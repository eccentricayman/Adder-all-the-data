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

def convert_scores():
    lit = school_scores.get_all()
    ret = {}
    for litty in lit:
        ret[litty['State']['Name']] = litty
        #print ret[litty['State']['Name']]
        #print "\n\n"
    return ret
'''
def corr_coef(drugs, school):
    return numpy.corrcoef(drugs,school)[0,1]
'''
print convert_scores()['New York']['Score Ranges'].keys()
