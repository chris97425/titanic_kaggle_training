import re

def check_all_group(x):
    if (x.Survived == 1).all():
        return "Rich."
    if (x.Survived == 0).all():
        return "Poor."
    else:
        return "other"

#Get the title of a name (mrs, ms etc) thanks to regex 👌🏼
def get_title(user_name):
    return  re.search(r', (.+?\.)',user_name).group(1)

#Define a class by age and sex
def class_of_people_by_age_sex(age, sex):
    print(sex)
    if age<=12:
        return "Children"
    elif age>=50 and sex==1:
        return "female_a_48"
    else :
        return "middle"
