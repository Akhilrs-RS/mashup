from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    def account_age(self):
        return 2025 - self.account_year

    @abstractmethod
    def get_role(self):
        pass


class Admin(User):
    def get_role(self):
        return "Admin"

    def __str__(self):
        return f"Admin User: {self.name} (Account created in {self.account_year})"


class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):
        return f"Guest User: {self.name} (Account created in {self.account_year})"


admin_user = Admin("Akhil", 2020)
guest_user = Guest("Rahul", 2023)

print(admin_user.get_role())
print(admin_user.account_age())
print(admin_user)

print(guest_user.get_role())
print(guest_user.account_age())
print(guest_user)