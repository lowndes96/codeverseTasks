#I thik this is what you were asking for, let me know if I've missunderstood the question. Thanks! 

class Recipient: 

    def __int__(self, email_adress, name, organisation): 
        self.email_adress = email_adress 
        self.name = name #could be broken down into first/middle/last 
        self.organisation = organisation

    def see_recipient(self):
        print(f"name: {self.name}, email adress: {self.email_adress} org: {self.organisation}")

    
class Label: 
    def __init__(self, name, colour): 
        self.name = name 
        self.colour = colour 

    def see_label(self):
        print(f"lable: {self.name}, colour: {self.colour}")

    def edit_name(self, new_name):
        self.name = new_name
    
    def edit_colour(self, new_colour): 
        self.colour = new_colour

    def create_sublabel(self, sub_name):
        return Sublabel(self.name, self.colour, sub_name)
    

class Sublabel(Label):
    #sub-label has option for more label text under variable sub_name  
        def __init__(self, name, colour, sub_name): 
            super().__init__(name, colour)
            self.sub_name = sub_name
        def see_sublabel(self):
            print(f"Sublabel: {self.name}, Colour: {self.colour}, Sub-name: {self.sub_name}")
class Mail: 

    def __init__(self, sender, recipients, subject, content, labels=None):
        self.sender = sender
        self.recipients = recipients  # List
        self.subject = subject
        self.content = content
        self.labels = labels or []  # List
        all_mail.append(self) #add each new mail to the global list

    def add_label(self, label):
        self.labels.append(label)

    def remove_label(self, label):
        self.labels.remove(label)


main_label = Label('main', 'red')
sub_1 = main_label.create_sublabel('sub_lab1')
sub_2 = sub_1.create_sublabel('sub_lab2')
