class Department:
    """Represents a department that an employee belongs to."""

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Department name cannot be blank")
        self.name = name.strip()

    def __str__(self):
        return self.name
