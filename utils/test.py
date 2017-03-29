import drugs
import school_scores

#----------------DRUG STUFF------------------------------------
def convert_drugs():
    lit = drugs.get_reports()
    ret = {}
    for litty in lit:
        ret[litty['State']] = litty
        print ret[litty['State']]
        print "\n\n"

#convert_drugs()

#--------------------------SCHOOL_SCORES---------------------------

def convert_scores():
    lit = school_scores.get_all()
    ret = {}
    for litty in lit:
        ret[litty['State']['Name']] = litty
        print ret[litty['State']['Name']]
        print "\n\n"

convert_scores()
