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



def find_state_drugs( code ):
    state = ""
    for stateName, cde in state_codes.items():
        if cde == code:
            state = stateName

    getAll = drugs.get_reports()
    returnVal = { }
    for year in range(2002, 2015, 1):
        itemDict = {}
        returnVal[ str(year) ] = itemDict
    for item in getAll:
        if item['State'] == state:
            itemDict = returnVal[ str(item['Year']) ]
            itemDict['Rates'] = {}
            itemDict['Rates']['Marijuana'] = item['Rates']['Marijuana']['Used Past Year']['12-17']
            itemDict['Rates']['Illicit Drugs'] = item['Rates']['Illicit Drugs']['Dependence Past Year']['12-17']
            itemDict['Rates']['Alcohol'] = item['Rates']['Alcohol']['Dependence Past Year']['12-17']
    return returnVal

def find_national_drugs():
    getAll = drugs.get_reports()
    returnVal = { }
    for year in range(2002, 2015, 1):
        itemDict = {}
        itemDict['Sums'] = { }
        itemDict['Sums']['Marijuana'] = 0
        itemDict['Sums']['Illicit Drugs'] = 0
        itemDict['Sums']['Alcohol'] = 0
        itemDict['Sums']['Population'] = 0
        itemDict['Rates'] = { }
        itemDict['Rates']['Marijuana'] = 0
        itemDict['Rates']['Illicit Drugs'] = 0
        itemDict['Rates']['Alcohol'] = 0
        returnVal[ str(year) ] = itemDict
    for item in getAll:
        itemDict = returnVal[ str(item['Year']) ]
        itemDict['Sums']['Marijuana'] += item['Totals']['Marijuana']['Used Past Year']['12-17']*10
        itemDict['Sums']['Illicit Drugs'] += item['Totals']['Illicit Drugs']['Dependence Past Year']['12-17']*10
        itemDict['Sums']['Alcohol'] += item['Totals']['Alcohol']['Dependence Past Year']['12-17']*10
        itemDict['Sums']['Population'] += item['Population']['12-17']
    for key in returnVal.keys():
        itemDict = returnVal[key]
        itemDict['Rates']['Marijuana'] = round( itemDict['Sums']['Marijuana'] * 10000.0 / itemDict['Sums']['Population'] ) / 100
        itemDict['Rates']['Illicit Drugs'] = round( itemDict['Sums']['Illicit Drugs'] * 10000.0 / itemDict['Sums']['Population'] ) / 100
        itemDict['Rates']['Alcohol'] = round( itemDict['Sums']['Alcohol'] * 10000.0 / itemDict['Sums']['Population'] ) / 100

    return returnVal

#print find_national_drugs()
#print find_state_drugs( 'CA' )
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

def find_state_scores(state):
    getAll = school_scores.get_all()
    returnVal = { }
    for year in range(2005, 2016, 1):
        itemDict = { }
        returnVal[ str(year) ] = itemDict
    for item in getAll:
        if item['State']['Code'] == state:
            itemDict = returnVal[str(item['Year'])]
            itemDict['State'] = state
            itemDict['Year'] = item['Year']
            itemDict['Averages'] = {}
            itemDict['Averages']['SAT'] = item['Total']['Verbal'] + item['Total']['Math']
            itemDict['Averages']['GPA'] = calculate_GPA( item['GPA'] )
    return returnVal

def calculate_GPA( insertDict ):
    numStudents = 0
    calculateSum = 0
    checkerList = ['A', 'B', 'C']
    for checker in checkerList:
        numStudents += insertDict[checker]['Test-takers']
        calculateSum += ( 69 - ord(checker) ) * insertDict[checker]['Test-takers']
    return round( calculateSum * 1.0 / numStudents * 10 ) / 10


def find_national_scores():
    getAll = school_scores.get_all()
    returnVal = { }  
    for year in range(2005, 2016, 1):
        itemDict = {}
        itemDict['Sums'] = { }
        itemDict['Sums']['SAT'] = 0
        itemDict['Sums']['GPA'] = 0
        itemDict['Sums']['SAT-Total'] = 0
        itemDict['Sums']['GPA-Total'] = 0
        itemDict['Averages'] = { }
        itemDict['Averages']['SAT'] = 0
        itemDict['Averages']['GPA'] = 0
        returnVal[ str(year) ] = itemDict
    for item in getAll:
        itemDict = returnVal[ item['Year'] ]
        itemDict['Sums']['SAT'] += (item['Total']['Verbal'] + item['Total']['Math']) * item['Total']['Test-takers']
        itemDict['Sums']['SAT-Total'] += item['Total']['Test-takers']

        ##GPA calcs
        checkerList = ['A', 'B', 'C']
        for checker in checkerList:
            itemDict['Sums']['GPA'] += ( 69 - ord(checker) ) * item['GPA'][checker]['Test-takers']
            itemDict['Sums']['GPA-Total'] += item['GPA'][checker]['Test-takers']

    for key in returnVal.keys():
        itemDict = returnVal[key]
        itemDict['Averages']['SAT'] = round( itemDict['Sums']['SAT'] * 1.0 / itemDict['Sums']['SAT-Total'] * 10 ) / 10
        itemDict['Averages']['GPA'] = round( itemDict['Sums']['GPA'] * 1.0 / itemDict['Sums']['GPA-Total'] * 10 ) / 10
        
    return returnVal
    
#find_scores( 'NY' )

#==========================CORRELATING===============

converted_drugs = convert_drugs()

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
        this_drugs = converted_drugs[state][str(year)]
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
