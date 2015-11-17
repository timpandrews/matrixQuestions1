#--- beginning of code ---
class Attendee(object):
     def __init__(self, name, fee):
         self.name = name
         self.fee = fee
         print "a:", self.name, self.fee

class Meeting(object):
     def __init__(self, name, attendees):
         self.name = name
         #self.attendees = list(attendees)
         input = list(attendees)
         print type(input)

         noDupesOutput = []
         print type(noDupesOutput)
         for attendee in input:
            print "b:  ", attendee.name, attendee.fee
            if attendee.name not in noDupesOutput:
                print "add"
                noDupesOutput.append(attendee)
            else:
                print "dupe"

         self.attendees = noDupesOutput




     def add_attendee(self, person):
         if person in self.attendees:
             print "Duplicate"
         else:
             print "Add"
             self.attendees.append(person)
     def calculate_fees(self):
         return sum(a.fee for a in self.attendees)
     def how_many_lunches_needed(self):
         return len(self.attendees)


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

