"""Run Practical 7: Inheritance, Composition & Packaging."""

from staff_app import Department, Developer


def main():
    engineering = Department("Engineering")
    dev = Developer("Riya", "EMP101", engineering, "Python")
    dev.salary = 65000

    print(dev.describe())
    print("Salary:", dev.salary)

    try:
        dev.salary = -100
    except ValueError as error:
        print("Validation:", error)


if __name__ == "__main__":
    main()
