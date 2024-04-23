class CustomerProfile:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
    
    def update_profile(self, name="shreyank", email="shreyankpatel032@gmail.com", phone_number="7338166834"):
        if name:
            self.name = name
        if email:
            self.email = email
        if phone_number:
            self.phone_number = phone_number
    
    def display_profile(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone Number:", self.phone_number)

customer1 = CustomerProfile("shreyank", "shreyank032@gmail.com", "7338166834")

customer1.display_profile()

customer1.update_profile(name="shreyankpatel",email="shreryankpatel032@gmail.com", phone_number="9876543210")

customer1.display_profile()
