import graphene
import expenses.schema
import employees.schema


class Query(employees.schema.Query, expenses.schema.Query, graphene.ObjectType):
    pass


class Mutation(expenses.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)