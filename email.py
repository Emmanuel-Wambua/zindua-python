class Email:
    has_been_read = False
    def __init__(self,email_address,subject_line,email_content):
        self.email = email_address
        self.subject = subject_line
        self.content = email_content
    def mark_as_read(self):
        Email.has_been_read = True
    def get_subject(self):
        return self.subject
    def read_emails():
        

class EmailManagement:
    def __init__(self):
        self.inboxes = []
    def populate_inbox(self,inbox):
        self.inboxes.append(inbox)
    def show_emails(self):
        for index,mail in enumerate(self.inboxes):
            sub = mail.get_subject()
            print(f"{index + 1}: {sub}")
    def read_email(self,index):
        self.index = index
        return self.inboxes[index].email

dummy1 = Email("mantelmanu31@gmail.com","Excursion","Go on a date with the homies")
dummy1.mark_as_read()
dummy2 = Email("charles69@gmail.com","Impossible","Go on a date with a girl")
dummy2.mark_as_read()
dummy3 = Email("cheli98@gmail.com","Realityt","Stop being deluded")

invent = EmailManagement()
invent.populate_inbox(dummy1)
invent.populate_inbox(dummy2)
invent.populate_inbox(dummy3)

# print(invent.inboxes[1].email)
print(invent.show_emails())
# print(invent.read_email(2))