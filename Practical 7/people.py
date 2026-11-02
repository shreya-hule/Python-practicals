from .department import Department


class Person:
    """Base class for a person."""

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be blank")
        self.name = name.strip()

    def describe(self):
        return f"Person: {self.name}"


class Employee(Person):
    """An employee is a person and has a department."""

    def __init__(self, name, employee_id, department):
        super().__init__(name)

        if not isinstance(employee_id, str) or not employee_id.strip():
            raise ValueError("Employee ID cannot be blank")
        if not isinstance(department, Department):
            raise TypeError("department must be a Department object")

        self.employee_id = employee_id.strip()
        self.department = department
        self._salary = 0.0

    @property
    def salary(self):
        """Return the employee's salary."""
        return self._salary

    @salary.setter
    def salary(self, amount):
        if amount < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = float(amount)

    def describe(self):
        return (
            f"Employee: {self.name}, ID: {self.employee_id}, "
            f"Department: {self.department}"
        )


class Developer(Employee):
    """A developer is an employee with a programming language."""

    def __init__(self, name, employee_id, department, language):
        super().__init__(name, employee_id, department)
        if not isinstance(language, str) or not language.strip():
            raise ValueError("Programming language cannot be blank")
        self.language = language.strip()

    def describe(self):
        return (
            f"{super().describe()}, "
            f"Role: Developer, Language: {self.language}"
        )
