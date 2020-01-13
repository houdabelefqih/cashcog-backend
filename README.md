
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

  _Example : I want all expenses that have "deli" in their description with a total amount less than or equal to 100_
 
  ```
     query {
       expenses(description_Icontains: "deli", amount_Lte : 100) {
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
     updateExpense(uuid: "", status: "approved"){
          uuid
          description
          status
        }
      }

```
 

#### Employees:

- To query all employees in the database:

```
    query employees{
      edges{
        node{
          uuid
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
       employees(lastName_Istartswith: "A", firstName_Icontains: "Isa") {
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
 
 _Example: Give me all employees whose last name starts with an "A", and first name contains "Isa". If they have expenses, only give me the approved ones that were created on Jan 07, 2020 with a total amount <= 100._  
 
  ```
     query {
       employees(lastName_Istartswith: "A", firstName_Icontains: "Isa") {
         edges {
           node {
             uuid
             firstName
             lastName
             expenses(amount_Lte : 100, createdAt_Date: "2020-01-07", status: "approved"){
              edges {
                 node {
                   uuid
                   description
                   approved
                   createdAt
                 }
                }
               }
              }
         }
       }
     }

  ```
 
