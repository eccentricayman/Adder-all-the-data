import drugs
import school_scores
#import numpy

state_codes = {
    'Mississippi': 'MS',
    'Northern Mariana Islands': 'MP',
    'Oklahoma':'OK',
    'Wyoming': 'WY',
    'Minnesota': 'MN',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arkansas': 'AR',
    'New Mexico': 'NM',
    'Indiana': 'IN',
    'Maryland': 'MD',
    'Louisiana': 'LA',
    'Texas': 'TX',
    'Tennessee': 'TN',
    'Iowa': 'IA',
    'Wisconsin': 'WI',
    'Arizona': 'AZ',
    'Michigan': 'MI',
    'Kansas': 'KS',
    'Utah': 'UT',
    'Virginia': 'VA',
    'Oregon': 'OR',
    'Connecticut': 'CT',
    'District of Columbia':'DC',
    'New Hampshire': 'NH',
    'Idaho': 'ID',
    'West Virginia':'WV',
    'South Carolina': 'SC',
    'California': 'CA',
    'Massachusetts': 'MA',
    'Vermont': 'VT',
    'Georgia': 'GA',
    'North Dakota': 'ND',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Florida': 'FL',
    'Hawaii': 'HI',
    'Kentucky': 'KY',
    'Rhode Island': 'RI',
    'Nebraska': 'NE',
    'Missouri': 'MO',
    'Ohio': 'OH',
    'Alabama': 'AL',
    'Illinois': 'IL',
    'Virgin Islands': 'VI',
    'South Dakota': 'SD',
    'Colorado': 'CO',
    'New Jersey': 'NJ',
    'National': 'NA',
    'Washington': 'WA',
    'North Carolina': 'NC',
    'Maine': 'ME',
    'New York': 'NY',
    'Montana': 'MT',
    'Nevada': 'NV',
    'Delaware': 'DE',
    'Guam': 'GU'
}
#---------------------------DRUG STUFF------------------------------------
states_drugs = drugs.get_reports()

def convert_drugs():
    overall = {}
    for state in states_drugs:
        name = state_codes[state['State']]
        if not name in overall.keys():
            overall[name] = {}
        weighted_data = [state['Totals']['Marijuana']['Used Past Year']['12-17']*1000,
        state['Totals']['Pain Relievers Abuse Past Year']['12-17']*1000,
        state['Totals']['Illicit Drugs']['Dependence Past Year']['12-17']*1000,
        state['Totals']['Alcohol']['Dependence Past Year']['12-17']*1000]
        overall[name][str(state['Year'])] = weighted_data
    return overall

drugs = convert_drugs()

#--------------------------SCHOOL_SCORES---------------------------------
let_to_num = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.1}
states_school = school_scores.get_all()

def convert_scores():
    overall = {}
    for state in states_school:
        weighted_data = []
        name = state['State']['Code']
        if not name in overall.keys():
            overall[name] = {}
        for letter in state['GPA']:
            if letter in let_to_num.keys():
                pt = let_to_num[letter]*400 + int(state['GPA'][letter]['Math']) + int(state['GPA'][letter]['Verbal'])
                for i in range(0,int(state['GPA'][letter]['Test-takers'])/2):
                    weighted_data.append(pt)
        overall[name][str(state['Year'])] = weighted_data
    return overall

scores = convert_scores()

#convert_scores(2014)['NY']
#print len(convert_scores(2014)['NY'])
#convert_drugs(2014)['NY']

def find_scores(state):
    states = school_scores.get_all()
    print states 
    returnVal = { }

find_scores( 'NY' )
    
#==========================CORRELATING===============

def scale_data(school, drugs):
    drugs = sorted(drugs)
    orig_len = len(drugs)
    for i in range(orig_len):
        for ctr in range(((len(school)-orig_len)/orig_len)+1):
            drugs.append(drugs[i])
    while len(drugs)>len(school):
        drugs.pop(len(drugs)-1)
    return drugs

def corr(year, state):
    try:
        this_drugs = drugs[state][str(year)]
        this_scores = scores[state][str(year)]
        this_drugs = scale_data(this_scores, this_drugs)
        r = abs(numpy.corrcoef(this_scores,this_drugs)[0][1])
        if not isinstance(r, float):
            return 0.0
        else:
            return r
    except:
        return 0.0

def state_corrs(year):
    ret = {}
    for state in state_codes:
        num = corr(year, state_codes[state])
        print "num %s type %s"%(str(num), type(num))
        if numpy.isnan(num):
            num = 0.0
        ret[state_codes[state]] = num
    return ret
