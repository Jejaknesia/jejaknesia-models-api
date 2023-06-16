# ML Endpoint API

This API serves as an endpoint for making predictions using TensorFlow Lite and TensorFlow models. It provides two accessible routes.

## Route 1: Predict Place

### Description

This route is used to predict a place based on the input text using the TensorFlow Lite model.

### Endpoint

```
POST /predict_place
```

### Request Parameters

| Name  | Type   | Description                    |
|-------|--------|--------------------------------|
| req   | JSON   | Request object containing text data |

#### Sample Request

```json
{
  "data": "category"
}
```

### Response Parameters

| Name      | Type   | Description                             |
|-----------|--------|-----------------------------------------|
| status    | string | Response status ("success" if successful) |
| error     | bool   | Indicates if an error occurred or not    |
| result    | array  | Prediction result (string array)         |

#### Sample Response

```json
{
  "status": "success",
  "error": false,
  "result": [
    "Place 1",
    "Place 2",
    "Place 3"
  ]
}
```

## Route 2: Predict Places

### Description

This route is used to predict multiple places based on a list of input texts using the TensorFlow model.

### Endpoint

```
POST /predict_places
```

### Request Parameters

| Name  | Type     | Description                            |
|-------|----------|----------------------------------------|
| req   | JSON     | Request object containing list of text data |

#### Sample Request

```json
{
  "data": [
    "category1",
    "category2",
    "category3"
  ]
}
```

### Response Parameters

| Name      | Type   | Description                              |
|-----------|--------|------------------------------------------|
| status    | string | Response status ("success" if successful) |
| error     | bool   | Indicates if an error occurred or not     |
| result    | array  | Prediction results (string array)         |

#### Sample Response

```json
{
  "status": "success",
  "error": false,
  "result": [
    "Place 1",
    "Place 2",
    "Place 3"
  ]
}
```

## Error Handling

If an error occurs during the prediction process, the API will respond with a status code of 500 and the message "Internal Server Error".

That's a brief documentation for the given API. You can add it to your README.md file on GitHub. Make sure to include information about installation, dependencies, and how to use the API.
