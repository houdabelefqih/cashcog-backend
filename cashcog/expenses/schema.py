import graphene
from graphene_django import DjangoObjectType

from expenses.models import Expense
from employees.schema import EmployeeType


class ExpenseType(DjangoObjectType):
    class Meta:
        model = Expense


class Query(graphene.ObjectType):
    expenses = graphene.List(ExpenseType)

    def resolve_expenses(self, info, **kwargs):
        return Expense.objects.all()


class ExpenseMutation(graphene.Mutation):

    uuid = graphene.UUID()
    description = graphene.String()
    created_at = graphene.DateTime()
    amount = graphene.Decimal()
    currency = graphene.String()
    employee = graphene.Field(EmployeeType)
    approved = graphene.Boolean()

    class Arguments:
        uuid = graphene.UUID()
        approved = graphene.Boolean()

    def mutate(self, info, uuid, approved):
        expense = Expense.objects.get(pk=uuid)
        expense.approved = approved
        expense.save()
        return ExpenseMutation(expense=expense)


class Mutation(graphene.ObjectType):
    update_expense = ExpenseMutation.Field()
