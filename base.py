#given a list of meetings, each of which has a list of attendees, 
# select a subset of those meetings which

#don't double book attendees
#maximizes total attendees across subset


#attendees = integers
#meetings = list of integers
#group of meetings, list of lists


# OUTOUT -> selected meetings and count of attendees. 


"""QUESTION: how do we identify meetings we should suggest to move

attack plan: move LARGEST meeting first - add attendees to a set - in meetings -
    (sets would speed up time required to see if somebody is in a meeting especially if 
    meeting attendees list grows exponentially)
loop through searching for largest meeting. 


build a funciton to find largest meeting and move it to 'reschedule' section. add 
all memebers to set of attendees. 
recursively call function passing in sliced list which would return nothing, but would 
add all necessary meetings and attendees to appropriate sets/lists

would it be better to sort meetings into size categories first?
not sure. I don't think it's necessary.

I will sort the list then if it's in order of shortest to longest, we can work of the end 
    of the list which is faster than the front

"""

def meetings_to_reschedule(meetings):
    """determine meetings which should be rescheduled from a list of meetings"""
    #sorts list of meetings by size, shortest to largest
    meetings_by_size = list(sorted(meetings, key=len))

    reschedule = []
    attendees = set()


    for num in range(1, len(meetings_by_size)):
        attended = False
        to_add = set()
        for person in meetings_by_size[-num]:
            if person in attendees:
                attended = True
            else:
                to_add.add(person)
        if attended == False:
            reschedule.append(meetings_by_size[-num])
            for pers in meetings_by_size[-num]:
                attendees.add(pers)

    print(f'Reschedule the following meetings: {reschedule}')
    print(f'This will affect {len(attendees)} employees')





Test1 = [[71,61,26],[72,75,76],[73,54,64,10,68],[88,56,69],[71,17,8],[18],[40,17,66,47,13],[40,62,52,88],[11,79,36,58,15],[17,67],[33],[38],[3,4,5,55,59,60,61,82,18,85,26,48,50],[17,84],[74,83,43],[71,89,27],[11,79,46,58],[34,33],[71,75,35],[66,14],[72,33],[75,76],[19,77,27],[40,72,75,44,7,35,20],[18,34],[71,17,33,67],[29,86,65,78,87,22,23,47,16,28],[38,37,27],[30,18,6,52,85,55],[79,28,58],[17,88,69],[76,23],[39,32,75],[29,86,65,78,87,22,47,23,16,28],[11,79,58],[21,88,51],[38],[61,88],[3,18],[39,0,24,23],[33,70],[42,75,7,35,20,37,80],[38,1,49],[31,12,88],[39,40,43],[33,56],[33,25],[33],[2,56],[52,85],[52,9,45,57],[53,33],[66,27],[63,88],[81,41,42,7,20]]
meetings_to_reschedule(Test1)



