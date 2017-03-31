import drugs
import school_scores
#import numpy

#---------------------------DRUG STUFF------------------------------------
def convert_drugs():
    lit = drugs.get_reports()
    ret = {}
    for litty in lit:
        ret[litty['State']] = litty
        #print ret[litty['State']]
        #print "\n\n"
    return ret

#print convert_drugs()['New York']
#List of info given by each state (seperated into age groups -- we focus on 12-17)
#Totals: 'Marijuana', 'Pain Relievers Abuse Past Year', 'Illicit Drugs', 'Tobacco', 'Alcohol'
#


#--------------------------SCHOOL_SCORES---------------------------------
let_to_num = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.1}

def convert_scores():
    states = school_scores.get_all()
    ret = {}
    for state in states: #FOR EACH STATE
        weighted_data = []
        for letter in state['GPA']: #FOR EACH GPA
            if letter in let_to_num.keys():
                if state['Year'] == '2014':
                    math_pt = let_to_num[letter]*200 + int(state['GPA'][letter]['Math'])
                    verbal_pt = let_to_num[letter]*200 + int(state['GPA'][letter]['Verbal'])
                    if state['State']['Code']=='NY':
                        print "SCORES %s: Math %d, Verbal %d"%(letter, math_pt, verbal_pt)
                    for i in range(0,int(state['GPA'][letter]['Test-takers'])/2): #FOR EACH TEST TAKER
                        # add average
                        # this puts it on 0-100 which i like
                        weighted_data.append(math_pt)
                        weighted_data.append(verbal_pt)
                    ret[state['State']['Code']] = weighted_data
    return ret
'''
def corr_coef(drugs, school):
    return numpy.corrcoef(drugs,school)[0,1]
'''

convert_scores()['NY']
