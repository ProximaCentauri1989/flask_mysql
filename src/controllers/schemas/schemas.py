user_schema = {
    "type": "object",
    "properties": {
        "username": { "type": "string" },
        "email" : { "type": "string" },
        "password" : { "type": "string"  },   
    },
    "required": ["username", "email", "password"]
}

payment_schema = {
    "type": "object",
    "properties": {
        "tx_id": { "type": "string" },
        "user_id" : { "type": "integer" },
    },
    "required": ["tx_id", "user_id"]
}
