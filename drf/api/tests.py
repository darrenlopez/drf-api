from rest_framework.test import APIRequestFactory

# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
request = factory.post('/api/customers/', {
    "customer": {
      "id": "b73b8b0e-0240-42a9-874c-00445d51dd8a",
      "first_name": "Ernest",
      "last_name": "Hemingway",
      "address_1": "907 Whitehead St",
      "address_2": "",
      "city": "Key West",
      "state": "FL",
      "postal_code": "33043",
      "subscription": {
        "id": "eac8709f-d898-42f0-84d8-a1997c25cae9",
        "plan_name": "print & digital",
        "price": "5999",
      },    
      "gifts":[
        {
          "id": "53368db4-6097-49c6-ba8b-b00ab4a3ce3b",
          "plan_name": "digital",
          "price": "4999",
          "recipient_email": "mark@twain.com"
        },
        {
          "id": "fb7a077b-928f-4d44-a2e5-6969c72d3b45",
          "plan_name": "digital",
          "price": "4999",
          "recipient_email": "jane@austin.com"
        }
      ]
    }
  })