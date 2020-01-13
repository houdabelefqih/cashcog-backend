import pytest
from employees.models import Employee
from expenses.models import Expense


@pytest.fixture()
def graphql_client():
    from graphene.test import Client
    import sys
    print(sys.path)

    from cashcog.schema import schema

    return Client(schema)


@pytest.fixture()
def employee():
    return Employee.objects.create(first_name="Houda", last_name="Belefqih")


@pytest.fixture()
def generate_employees():
    employee_1 = Employee.objects.create(first_name="Houda", last_name="Belefqih")

    employee_2 = Employee.objects.create(first_name="Armin", last_name="Van Buuren")

    employee_3 = Employee.objects.create(first_name="Paul", last_name="Van Dyk")

    employee_4 = Employee.objects.create(first_name="Ferry", last_name="Corsten")

    employee_5 = Employee.objects.create(first_name="Paul", last_name="Oakenfold")

    employee_6 = Employee.objects.create(first_name="Tijs", last_name="Verwest")

    employee_7 = Employee.objects.create(first_name="Markus", last_name="Shulz")

    return employee_1, employee_2, employee_3, employee_4, employee_5, employee_6, employee_7


@pytest.fixture()
def generate_expenses():
    employee_1 = Employee.objects.create(first_name="Houda", last_name="Belefqih")

    employee_2 = Employee.objects.create(first_name="Armin", last_name="Van Buuren")

    employee_3 = Employee.objects.create(first_name="Paul", last_name="Van Dyk")

    employee_4 = Employee.objects.create(first_name="Ferry", last_name="Corsten")

    employee_5 = Employee.objects.create(first_name="Paul", last_name="Oakenfold")

    employee_6 = Employee.objects.create(first_name="Tijs", last_name="Verwest")

    expense1 = Expense.objects.create(description="Itaque fugiat repellendus velit deserunt praesentium.",
                                      amount=100,
                                      currency='MAD',
                                      created_at="2019-09-22T23:07:01",
                                      employee=employee_1)

    expense2 = Expense.objects.create(description="Dolorem dignissimos optio nobis laborum.",
                                      amount=2759,
                                      currency='UGX',
                                      created_at="2019-12-29T11:06:01",
                                      employee=employee_2)

    expense3 = Expense.objects.create(description="Reiciendis fugiat cum minima magni vero deserunt.",
                                      amount=1189,
                                      currency='HKD',
                                      created_at="2020-01-01T10:15:09", employee=employee_3)

    expense4 = Expense.objects.create(description="Minus alias rem labore voluptates voluptatum.",
                                      amount=27,
                                      currency='CUC',
                                      created_at="2020-01-01T11:20:30", employee=employee_4)

    expense5 = Expense.objects.create(description="Delectus corporis laudantium sunt.",
                                      amount=9334,
                                      currency='SAR',
                                      created_at="2020-01-05T06:39:40", employee=employee_5)

    expense6 = Expense.objects.create(description="Dolorum magni qui deserunt corrupti.",
                                      amount=7841,
                                      currency='STD',
                                      created_at="2019-09-22T23:07:01", employee=employee_6)

    expense7 = Expense.objects.create(description="Velit sit repellat nisi.",
                                      amount=852,
                                      currency='IDR',
                                      created_at="2019-09-22T23:07:01", employee=employee_6)

    return expense1, expense2, expense3, expense4, expense5, expense6, expense7


@pytest.fixture()
def expense():
    expense_employee = Employee.objects.create(first_name="Houda", last_name="Belefqih")

    expense = Expense.objects.create(description="Itaque fugiat repellendus velit deserunt praesentium.",
                                     amount=100,
                                     currency='MAD',
                                     created_at="2019-09-22T23:07:01",
                                     employee=expense_employee)

    return expense
