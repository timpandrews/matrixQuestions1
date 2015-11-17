'''
Q1-1.
Change the Meeting class so that the same person will not
appear twice as an attendee, even if accidentally entered twice.
'''

class Attendee(object):
     def __init__(self, name, fee):
         self.name = name
         self.fee = fee

class Meeting(object):
     def __init__(self, name, attendees):
         self.name = name
         inputList = list(attendees)

         #DeDup original attendee list when Meeting Obj is first initiated
         attendee_names = set()
         noDuplicateAttendeeList = []
         for obj in inputList:
            if obj.name not in attendee_names:
                noDuplicateAttendeeList.append(obj)
                attendee_names.add(obj.name)

         self.attendees = noDuplicateAttendeeList

     def add_attendee(self, person):
         attendee_names = set()

         #Check to make sure new attendee is not a duplicate before appending to obj
         #Build list of existing attendee names
         for obj in self.attendees:
             attendee_names.add(obj.name)

         #Add new name if not duplicate
         if person.name not in attendee_names:
            self.attendees.append(person)

     def calculate_fees(self):
         return sum(a.fee for a in self.attendees)
     def how_many_lunches_needed(self):
         return len(self.attendees)


def main():
     #---Altered original attendee list to contain one duplicate---
     attendees = [
                   Attendee("John Allston", 50),
                   Attendee("Margaret Bristol", 50),
                   Attendee("George Voight", 30),
                   Attendee("Emily Green", 30),
                   Attendee("Chris Mortenson", 50),
                   Attendee("Pat Smith", 50),
                   Attendee("Pat Smith", 50),
                   ]

     our_meeting = Meeting("Major Conference", attendees)

     #---Add two additional attendees one of which is a duplicate---
     our_meeting.add_attendee(Attendee("John Sample", 30))
     our_meeting.add_attendee(Attendee("Pat Smith", 50))

     print "Total fees for the", our_meeting.name, "Event are: $", our_meeting.calculate_fees()

     print "\nAttendees for ", our_meeting.name
     for attendee in our_meeting.attendees:
         print "  ", attendee.name, ", $", attendee.fee

if __name__=="__main__":
     main()

