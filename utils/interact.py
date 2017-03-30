import drugs
import school_scores
#import numpy

#---------------------------DRUG STUFF------------------------------------
def convert_drugs():
    lit = drugs.get_reports()
    ret = {}
    for litty in lit:
        ret[litty['State']] = litty
        print ret[litty['State']]
        print "\n\n"
    return ret

print convert_drugs().keys()

#--------------------------SCHOOL_SCORES---------------------------------

def convert_scores():
    lit = school_scores.get_all()
    ret = {}
    for litty in lit:
        ret[litty['State']['Name']] = litty
        print ret[litty['State']['Name']]
        print "\n\n"
'''
def corr_coef(drugs, school):
    return numpy.corrcoef(drugs,school)[0,1]
'''
#convert_scores()
