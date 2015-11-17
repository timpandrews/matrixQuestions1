#--- beginning of code ---
class Attendee(object):
     def __init__(self, name, fee):
         self.name = name
         self.fee = fee
         print "a:", self.name, self.fee

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
            else:
                print "dupe"
         self.attendees = noDuplicateAttendeeList

     def add_attendee(self, person):
         print person.name
         attendee_names = set()

         #Check to make sure new attendee is not a duplicate before appending to obj
         #Build list of existing attendee names
         for obj in self.attendees:
             attendee_names.add(obj.name)

         #Add new name if not duplicate
         if person.name not in attendee_names:
            self.attendees.append(person)
         else:
            print "dupe"

     def calculate_fees(self):
         return sum(a.fee for a in self.attendees)
     def how_many_lunches_needed(self):
         return len(self.attendees)


def main():
     #Original attendee list contains one duplicate
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

     #Add two additional attendees one of which is a duplicate
     our_meeting.add_attendee(Attendee("John Sample", 30))
     our_meeting.add_attendee(Attendee("Pat Smith", 50))

     print "Total fees are: ", our_meeting.calculate_fees()
     print "lunches needed: ", our_meeting.how_many_lunches_needed()


if __name__=="__main__":
     main()

