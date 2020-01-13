
## Description:

Django application that consumes the expense events provided by the Cashcog Expense-API. Validates and stores them in a MySQL database.
It also provides a Graph-QL API allowing clients to fetch, update (approve or decline), and query these expenses.

## Run the app:

1. Have Docker installed and running on your machine.
2. In a terminal run :
  ``` docker-compose build ```
3. Then : 
``` docker-compose run ```

### Graphql queries examples:

#### Access API via: localhost:8000/cashcog/ ####

Either using a browser (which will redirect to the GraphiQL interface) or using your favorite REST/GraphQL client.

#### Expenses:

- To query all expenses in the database:

```
    query expenses{
      edges{
        node{
          uuid
          description
          createdAt
          amount
          currency
          status
          employee {
            uuid
            firstName
            lastName
          }   
        }
      }
    }

  }
 ```
 
- To query expenses based on a specific filter : 

  _Example : I want all expenses that have "tempore" in their description with a total amount less than or equal to 3000_
 
  ```
     query {
     expenses(description_Icontains: "tempore", amount_Lte : 3000) {
       edges {
         node {
          uuid
          description
          createdAt
          amount
          currency
          status
         }
       }
     }
         }

  ```
  
 **Filters for expenses are (according to Django's field lookups https://docs.djangoproject.com/en/3.0/ref/models/querysets/#id4):**
  
  * uuid: exact
  * description: iexact, icontains
  * created_at: date, week_day,year, month, day, time, hour
  * amount: exact, gt, gte, lt, lte
  * currency: iexact, icontains
  * status': iexact


- To approve or decline an expense : 
  _Inputs are : UUID of the expense, and a status (approved, declined). Status for each newly created expense is "pending" by default_

```

mutation {
  updateExpense(input: {uuid: "00f3c0c4-e97b-41bf-abc5-4ae716af992d",status: "approved"}){
    expense{
      uuid
      description
      amount
      status
    }
  }
}

```
 

#### Employees:

- To query all employees in the database:

```
 query {
  employees{
    edges{
      node{
        firstName
        lastName
        
      }
    }
  }
}
 ```
 
 - To query employees based on a specific filter : 
 
 
  ```
     query {
        employees(lastName_Istartswith: "S", firstName_Icontains: "Al") {
          edges {
            node {
              uuid
              firstName
              lastName
            }
          }
        }
      }

  ```
  
  **Filters for employees are (according to Django's field lookups https://docs.djangoproject.com/en/3.0/ref/models/querysets/#id4):**
  
    * uuid: exact
    * firstName: icontains, istartswith, iexact
    * lastName: icontains, istartswith, iexact
  
 - You can also do nested queries/filtering: 
 
 _Example: Give me all employees whose last name starts with an "S", and first name contains "al". If they have expenses, only give me the ones with a total amount in the range [1000-4000] in a currency that contains the letter "M"._  
 
  ```
    query {
      employees(lastName_Istartswith: "S", firstName_Icontains: "al") {
        edges {
          node {
            uuid
            firstName
            lastName
            expenses(currency_Icontains: "M",amount_Gte: 1000, amount_Lte: 4000) {
              edges {
                node {
                  uuid
                  description
                  status
                  amount
                  currency
                }
              }
            }
          }
        }
      }
}

  ```
 
