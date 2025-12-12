class Employee:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print("-" * 30)


class Trainer(Employee):
    def __init__(self, name: str, role: str, specialization: str):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")
        print("-" * 30)


class YogaInstructor(Employee):
    def __init__(self, name: str, role: str, yoga_style: str):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Yoga Style: {self.yoga_style}")
        print("-" * 30)


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name: str, role: str, specialization: str, yoga_style: str):
        # Initialize Employee directly, then set both extra attributes
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")
        print(f"Yoga Style: {self.yoga_style}")
        print("-" * 30)


# Sample objects
emp = Employee("Alice", "Receptionist")
trainer = Trainer("Bob", "Fitness Trainer", "Strength Training")
yoga = YogaInstructor("Carol", "Yoga Instructor", "Vinyasa")
multi = MultiTrainer("Dave", "Senior Trainer", "CrossFit", "Hatha")

# Display details
emp.display()
trainer.display()
yoga.display()
multi.display()