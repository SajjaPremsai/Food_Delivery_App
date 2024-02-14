# Food Delivery App API Documentation

## Overview
The Food Delivery App API provides endpoints for managing organizations, items, and pricing for delivery services.

## Base URL

https://food-delivery-app-wbgd.onrender.com


## Authentication
Authentication is required for certain endpoints. Please refer to the authentication section for details.

## Endpoints

### Organizations
- **GET** `/organizations/`: Retrieve all organizations.
- **POST** `/organizations/`: Create a new organization.
  
### Items
- **GET** `/items/`: Retrieve all items.
- **POST** `/items/`: Create a new item.
  
### Pricing
- **GET** `/pricing/`: Retrieve all pricing structures.
- **POST** `/pricing/`: Create a new pricing structure for an organization.
- **POST** `/delivery-charge/`: Calculate delivery charges based on input data.

## Sample Requests

### Create Organization

```json

POST /organizations/
{
  "name": "Example Organization"
}
```

### Create Items

```json
POST /items/
{
  "type": "perishable",
  "description": "Example Perishable Item"
}
```

### Create Pricing

```json
POST /pricing/
{
  "organization": 1,
  "item": 1,
  "zone": "East",
  "base_distance_in_km": 5,
  "km_price": 1.5,
  "fix_price": 10.0
}
```
### Create DeliveryCharge

```json
POST /delivery-charge/
{
  "organization_id": 1,
  "item_type": "perishable",
  "zone": "East",
  "total_distance": 10
}
```
