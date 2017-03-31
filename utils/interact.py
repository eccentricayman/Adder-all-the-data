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
def convert_drugs(year):
    states = drugs.get_reports()
    ret = {}
    for state in states:
        print "State: %s"%(state['State'])
        if state['Year'] == year:
            weighted_data = []
            ret[state_codes[state['State']]] = weighted_data
            print state['Totals']['Marijuana']['Used Past Year']['12-17']*1000
            print state['Totals']['Pain Relievers Abuse Past Year']['12-17']*1000
            print state['Totals']['Illicit Drugs']['Dependence Past Year']['12-17']*1000
            print state['Totals']['Alcohol']['Dependence Past Year']['12-17']*1000
            # find stuff for diff rates, idk why theyre formatted diff :(
    return ret

#print convert_drugs()['New York']
#List of info given by each state (seperated into age groups -- we focus on 12-17)
#Totals: 'Marijuana', 'Pain Relievers Abuse Past Year', 'Illicit Drugs', 'Tobacco', 'Alcohol'
#


#--------------------------SCHOOL_SCORES---------------------------------
let_to_num = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.1}

def convert_scores(year):
    states = school_scores.get_all()
    ret = {}
    for state in states: #FOR EACH STATE
        weighted_data = []
        for letter in state['GPA']: #FOR EACH GPA
            if letter in let_to_num.keys() and state['Year'] == str(year):
                math_pt = let_to_num[letter]*200 + int(state['GPA'][letter]['Math'])
                verbal_pt = let_to_num[letter]*200 + int(state['GPA'][letter]['Verbal'])
                for i in range(0,int(state['GPA'][letter]['Test-takers'])/2): #FOR EACH TEST TAKER
                    # add average
                    # this puts it on 0-100 which i like
                    weighted_data.append(math_pt)
                    weighted_data.append(verbal_pt)
                ret[state['State']['Code']] = weighted_data
    return ret

#convert_scores(2014)['NY']
print len(convert_scores(2014)['NY'])
convert_drugs(2014)['NY']
