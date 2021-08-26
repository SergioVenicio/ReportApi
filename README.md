# ReportApi

## Endpoints
#### /transactions/<transaction_id>
#### /transactions/list
Parameters: 
| name | type  | required |
| :------------ |:---------------:| -----:|
| from_date     | date ||
| to_date       | date ||
| status        | text ||
| operation     | text ||
| merchant_id   | text ||
| acquirer_id   | text ||
| payment_method| text ||
| error_code    | text ||
| filter_field  | text ||
| filterValue   | text ||
| page          | int ||
#### /transactions/report
Parameters: 
| name | type  | required |
| :------------ |:---------------:| -----:|
| from_date     | date | x |
| to_date       | date | x |
| merchant      | text ||
| acquirer     | text ||
| payment_method   | text ||