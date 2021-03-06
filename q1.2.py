
#Note: Solution for Q1-2 includes deduping improvements from Q1-1

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


class BigWigMeeting(Meeting):
    def __init__(self, name, attendees):

        #Automatically add Big Wig to attendee list with a $50 fee
        bigWig = Attendee("Big Wig", 50)
        attendees.append(bigWig)

        Meeting.__init__(self, name, attendees)

    def calculate_netIncome(self):
        return sum((a.fee - 30) for a in self.attendees)


def main():

     #--- Build original attendee list for Big Wig Retreat one of which is a duplicate ---
     bigWigs = [
                   Attendee("Jo Jackson", 50),
                   Attendee("Richard Herrera", 50),
                   Attendee("Marie Montgomery", 30),
                   Attendee("Brian Sims", 30),
                   Attendee("Debra Adams", 50),
                   Attendee("Pat Smith", 50),
                   Attendee("Pat Smith", 50),
                   ]

     our_bigwig_meeting = BigWigMeeting("BigWig Retreat", bigWigs)

     #--- Add two additional attendees to Big Wig Retreat one of which is a duplicate ---
     our_bigwig_meeting.add_attendee(Attendee("Sharon Conway", 30))
     our_bigwig_meeting.add_attendee(Attendee("Pat Smith", 50))

     #--- Print out total fees & net income for Big Wig Retreat ---
     print "Total fees for the", our_bigwig_meeting.name, "Event are: $", our_bigwig_meeting.calculate_fees()
     print "Net income for the", our_bigwig_meeting.name, "Event is: $", our_bigwig_meeting.calculate_netIncome()

     print "\nAttendees for", our_bigwig_meeting.name
     for attendee in our_bigwig_meeting.attendees:
         print "  ", attendee.name, ", $", attendee.fee

if __name__=="__main__":
     main()
