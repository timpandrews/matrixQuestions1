#--- beginning of code ---
class Attendee(object):
     def __init__(self, name, fee):
         self.name = name
         self.fee = fee
         #print self.name

class Meeting(object):
     def __init__(self, name, attendees):
         self.name = name
         self.attendees = list(attendees)
     def add_attendee(self, person):
         self.attendees.append(person)
         print self.name
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
                   ]
     our_meeting = Meeting("Major Conference", attendees)

     print "Total fees are: ", our_meeting.calculate_fees()
     print "lunches needed: ", our_meeting.how_many_lunches_needed()

if __name__=="__main__":
     main()

