

# Fast Food Fast Api Endpoints

Fast food fast API implementation details.

## How it Works
- A user can view available food items 
- A user chooses on a food item and makes an order
- A user can update a food item details
- An Admin can accept or reject the order request from a user
- Accepted orders are delivered to the user

## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtua Environment](https://virtualenv.pypa.io/en/stable/installation/)

# Installation and Setup

Clone the repository below

```
git clone https://github.com/Gabkings/flask-api-endpoints/tree/develop
```

### Create and activate a virtual environment

    virtualenv env --python=python3.7

    cd env/Script/activate

### Install required Dependencies

    pip install -r requirements.txt



## Endpoints Available

| Method | Endpoint                        | Description                           |
| ------ | ------------------------------- | ------------------------------------- |
| POST   | /api/v1/orders                  | post a fooditem                       |
| GET    | /api/v1/orders                  | get all available foods               |
| PUT    | /api/v1/orders/<{id}>           | update on the status of an order      |
| GET    | /api/v1/orders/<{id}>           | get a specific food order             |
| DELETE | /api/orders/<{id}>              | delete a specific order by id         | 
 
### Developed By :

Gabriel Gitonga
