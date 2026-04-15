# config/data_quality.py

DATA_QUALITY_PROFILE = {
    "customers": {
        "duplicate_rate": 0.3,
        "missing_email_rate": 0.5,
        "invalid_email_rate": 0.2,
        "missing_city_rate": 0.5
    },

    "orders": {
        "duplicate_rate": 0.3,
        "missing_product_rate": 0.3,
        "invalid_amount_rate": 0.3,
        "negative_amount_rate": 0.5,
        "invalid_status_rate": 0.4
    },

    "products": {
        "duplicate_rate": 0.3,
        "missing_name_rate": 0.4,
        "invalid_price_rate": 0.6,
        "zero_price_rate": 0.3,
        "category_mismatch_rate": 0.02,
        "schema_drift_rate": 0.05
        }
}
