import drugs
import school_scores
import numpy

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
    for year in range(2005,2015):
        ret = {}
        for state in states_drugs:
            #print "State: %s"%(state['State'])
            if state['Year'] == year:
                #ret[state_codes[state['State']]] = weighted_data
                weighted_data = [state['Totals']['Marijuana']['Used Past Year']['12-17']*1000,
                        state['Totals']['Pain Relievers Abuse Past Year']['12-17']*1000,
                        state['Totals']['Illicit Drugs']['Dependence Past Year']['12-17']*1000,
                        state['Totals']['Alcohol']['Dependence Past Year']['12-17']*1000]
                # find stuff for diff rates, idk why theyre formatted diff :(
                ret[state_codes[state['State']]] = weighted_data
        overall[year] = ret
    return overall

#print convert_drugs()['New York']
#List of info given by each state (seperated into age groups -- we focus on 12-17)
#Totals: 'Marijuana', 'Pain Relievers Abuse Past Year', 'Illicit Drugs', 'Tobacco', 'Alcohol'
#


#--------------------------SCHOOL_SCORES---------------------------------
let_to_num = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.1}
states_school = school_scores.get_all()

def convert_scores():
    overall = {}
    for year in range(2005,2015):
        ret = {}
        for state in states_school: #FOR EACH STATE
            weighted_data = []
            for letter in state['GPA']: #FOR EACH GPA
                if letter in let_to_num.keys() and state['Year'] == str(year):
                    pt = let_to_num[letter]*400 + int(state['GPA'][letter]['Math']) + int(state['GPA'][letter]['Verbal'])
                    for i in range(0,int(state['GPA'][letter]['Test-takers'])/2): #FOR EACH TEST TAKER
                        # add average
                        # this puts it on 0-100 which i like
                        weighted_data.append(pt)
                        #weighted_data.append(verbal_pt)
                    ret[state['State']['Code']] = weighted_data
        overall[year] = ret
    return overall

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
    drugs = convert_drugs()[year][state]
    scores = convert_scores()[year][state]
    drugs = scale_data(scores, drugs)
    return abs(numpy.corrcoef(scores,drugs)[0][1])

print corr(2005, 'VA')
