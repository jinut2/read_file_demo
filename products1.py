import os
import ujson as json

media = {
    "id" : 1231313,
    "default" : "true", #true / false,
    "variants" : [
        {
            "size" : "thumb", # thumb, low, normal, high, zoom,
            "url" : "here_url",
            "height" : 200,
            "width" : 200,
            "dpi" : 120
        }
    ]
}

contact = {
    "phone no." : 8989898989,
    "mail-id" : "no_one@nomail.com"
}

address = {}

merchant = {
    "merchant-id" : 1231313,
    "contact" :  contact ,
    "address" : address ,
    "rating" : 4.5,
    "rating-count" : 4
}

subscription = {
    "subscription-id": 123123131,
    "variant-id" : 124312313,
    "product-id" : 234132131,
    "base-price" : 30000.00,
    "offer-price" : 25000.00,
    "offer-valid-till" : "2015-07-30 T 23:59",
    "media" : [ media ],
    "condition" : "", #// ignore
    "payment-modes" : [ "cod", "pre-paid" ],
    "merchant" : merchant,
    "buy-box" : "true", #true / false,
    "shipping-hours" : 12,
    "lead-hours" : 12,
    "cod" : "true"
}

variant = {
    "product-id" : 234132131,
    "variant-id" : 124312313,
    "title" : "Samsung Galaxy S4 32 GB",
    "categories" : [ { "id": 123, "label": "mobile phones" } ],
    "subscriptions" : [subscription,subscription,subscription],
    "brand" : "samsung",
    "media" : [media],
    "user-rating" : 4.5,
    "rating-count" : 14,
    "expert-rating" : 4.5,
    "description" : "blah",
    "features" : "blah",
    "specification" : "blah",
    "attributes": [
        {
            "name" : "height",
            "display" : "Height",
            "values" : [ 20 ],
            "unit" : "cm",
            "variant" : "false"
        },
        {
            "name" : "RAM",
            "display" : "Memory",
            "values" : [ 32 ],
            "unit" : "GB",
            "variant" : "true" #// attribute used to create a variant
        }
    ]
}

product = {
    "product-id" : 234132131,
    "title" : "samsung galaxy s4",
    "categories" : [ { "id": 123, "label": "mobile phones" } ],
    "variants" : [variant,variant,variant],
    "brand" : "samsung",
    "media" : [media],
    "user-rating" : 4.5,
    "rating-count" : 14,
    "expert-rating" : 4.5,
    "description" : "blah",
    "features" : "blah",
}
