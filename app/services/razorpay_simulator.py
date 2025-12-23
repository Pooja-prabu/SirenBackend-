# import random

# def process_payment():
#     scenarios = [
#         {"gateway": "success", "bank": "success"},
#         {"gateway": "failed", "bank": "success"},
#         {"gateway": "failed", "bank": "failed"},
#         {"gateway": "timeout", "bank": "success"},
#     ]
#     return random.choice(scenarios)
import random

def process_payment():
    scenarios = [
        {"gateway_status": "success", "bank_status": "success"},
        {"gateway_status": "failed", "bank_status": "success"},
        {"gateway_status": "timeout", "bank_status": "success"},
        {"gateway_status": "failed", "bank_status": "failed"},
    ]
    return random.choice(scenarios)
