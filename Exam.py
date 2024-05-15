from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def calculate_salary(self) -> float:
        pass


class FixedSalaryEmployee(Employee):
    def __init__(self, name: str, monthly_salary: float):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self) -> float:
        return self.monthly_salary


class CommissionEmployee(Employee):
    def __init__(self, name: str, sales: float, commission_rate: float):
        super().__init__(name)
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_salary(self) -> float:
        return self.sales * self.commission_rate


class SalaryCommissionEmployee(Employee):
    def __init__(self, name: str, base_salary: float, sales: float, commission_rate: float):
        super().__init__(name)
        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_salary(self) -> float:
        return self.base_salary + (self.sales * self.commission_rate)


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def remove_employee(self, name: str):
        # Remove by filtering employees with names different from the target name
        self.employees = [emp for emp in self.employees if emp.name != name]
        print(f"Employee named {name} has been removed from the manager.")

    def calculate_total_payroll(self) -> float:
        total_payroll = 0.0
        for employee in self.employees:
            total_payroll += employee.calculate_salary()
        return total_payroll

    def print_payroll_report(self):
        print("Payroll Report:")
        for employee in self.employees:
            print(f"- {employee.name}: {employee.calculate_salary():.2f}")
        print(f"Total Payroll: {self.calculate_total_payroll():.2f}")


if __name__ == "__main__":
    employee_manager = EmployeeManager()

    employee_manager.add_employee(FixedSalaryEmployee("John", 3000))
    employee_manager.add_employee(FixedSalaryEmployee("Drake", 5000))
    employee_manager.add_employee(CommissionEmployee("Bob", 50000, 0.1))
    employee_manager.add_employee(CommissionEmployee("Alex", 120000, 0.1))
    employee_manager.add_employee(SalaryCommissionEmployee("Carol", 1000, 20000, 0.05))
    employee_manager.add_employee(SalaryCommissionEmployee("Kate", 2000, 10000, 0.04))

    employee_manager.print_payroll_report()

    # Remove employees and print updated report
    employee_manager.remove_employee("Bob")
    employee_manager.remove_employee("Kate")
    print("\nUpdated Payroll Report:")
    employee_manager.print_payroll_report()
