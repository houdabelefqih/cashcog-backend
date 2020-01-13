import json
import requests

from expenses.models import Expense
from employees.models import Employee

STREAM_URL = "https://cashcog.xcnt.io/stream"

r = requests.get(STREAM_URL, stream=True)

for line in r.iter_lines():

    if line:
        decoded_line = line.decode('utf-8')
        data = json.loads(decoded_line)

        employee = data.pop('employee')
        employee_obj, employee_created = Employee.objects.get_or_create(uuid=employee['uuid'], defaults=employee)
        expense_obj, expense_created = Expense.objects.get_or_create(
            uuid=data['uuid'],
            defaults={**data, 'employee': employee_obj}
        )

