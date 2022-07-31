# cat_toy_ranking

This service has one classify function, that takes an array with the following properties:

| Property | Data Type |
|----------|-----------|
| Shape::Circle | bit |
| Shape::Rectangle | bit |
| Shape::Square | bit |
| Softeness::Hard | bit |
| Softness::Medium | bit |
| Softnes::Soft | bit |

For example:

```shell
curl -X 'POST' \
  'http://127.0.0.1:3000/classify' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
  [0,1,0,0,1,0]
]'
```

Response body:
```json
[
 "High"
]
```