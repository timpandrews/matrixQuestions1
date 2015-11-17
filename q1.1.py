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
         attendee_names = set()
         noDuplicateAttendeeList = []
         for obj in inputList:
            if obj.name not in attendee_names:
                noDuplicateAttendeeList.append(obj)
                attendee_names.add(obj.name)
         self.attendees = noDuplicateAttendeeList

     def add_attendee(self, person):
         
         self.attendees.append(person)

     def calculate_fees(self):
         return sum(a.fee for a in self.attendees)
     def how_many_lunches_needed(self):
         return len(self.attendees)

class DeDupe(object):
    def __init__(self, attendees):
        self.attendees = attendees
        attendee_names = set()
        noDuplicateAttendeeList = []
        for obj in self.attendees:
            if obj.name not in attendee_names:
                noDuplicateAttendeeList.append(obj)
                attendee_names.add(obj.name)

        for x in noDuplicateAttendeeList:
            print "x   ", x.name

        return noDuplicateAttendeeList

def main():
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

     #our_meeting.add_attendee(Attendee("John Sample", 30))
     #our_meeting.add_attendee(Attendee("Pat Smith", 50))

     for attendee in our_meeting.attendees:
        print "c:    ", attendee.name, ", ", attendee.fee

     print

     print "Total fees are: ", our_meeting.calculate_fees()
     print "lunches needed: ", our_meeting.how_many_lunches_needed()




if __name__=="__main__":
     main()

