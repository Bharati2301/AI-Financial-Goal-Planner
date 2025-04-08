import os
import requests
from dotenv import load_dotenv

load_dotenv()

YODLEE_CLIENT_ID = os.getenv("YODLEE_CLIENT_ID")
YODLEE_SECRET = os.getenv("YODLEE_SECRET")
YODLEE_LOGIN_NAME = os.getenv("YODLEE_LOGIN_NAME")
YODLEE_API_BASE = "https://sandbox.api.yodlee.com/ysl"

TEST_USERNAME = os.getenv("YODLEE_TEST_USERNAME")
TEST_PASSWORD = os.getenv("YODLEE_TEST_PASSWORD")

def get_access_token():
    headers = {
        "Api-Version": "1.1",
        "loginName": YODLEE_LOGIN_NAME,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "clientId": YODLEE_CLIENT_ID,
        "secret": YODLEE_SECRET
    }
    response = requests.post(f"{YODLEE_API_BASE}/auth/token", headers=headers, data=data)
    json_data = response.json()
    token = json_data.get("token", {}).get("accessToken")
    if not token:
        raise Exception(f"[Yodlee] Auth failed:\n{json_data}")
    print("\n✅ Access token acquired.")
    return token.strip()

def delete_all_provider_accounts(token):
    headers = {
        "Api-Version": "1.1",
        "Authorization": f"Bearer {token}"
    }
    res = requests.get(f"{YODLEE_API_BASE}/providerAccounts", headers=headers)
    accounts = res.json().get("providerAccount", [])
    for acct in accounts:
        acct_id = acct["id"]
        del_res = requests.delete(f"{YODLEE_API_BASE}/providerAccounts/{acct_id}", headers=headers)
        print(f"🗑️ Deleted providerAccount {acct_id}: {del_res.status_code}")

def link_test_account(token):
    headers = {
        "Api-Version": "1.1",
        "Authorization": token,
        "Content-Type": "application/json"
    }
    body = {
        "providerId": 16441,
        "consentId": 1,
        "preferences": {
            "autoRefresh": True
        },
        "loginForm": {
            "id": 1,
            "formType": "login",
            "row": [
                {
                    "id": 1,
                    "field": [
                        {"id": "login", "value": TEST_USERNAME},
                        {"id": "password", "value": TEST_PASSWORD}
                    ]
                }
            ]
        }
    }
    res = requests.post(f"{YODLEE_API_BASE}/providerAccounts", headers=headers, json=body)
    print("📦 Link Account Response:", res.status_code, res.text)
    if res.status_code not in [200, 201]:
        raise Exception(f"[Yodlee] Failed to link Dag Site: {res.text}")

def fetch_transactions(income, expenses):
    try:
        token = get_access_token()
        delete_all_provider_accounts(token)
        link_test_account(token)

        headers = {
            "Api-Version": "1.1",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        response = requests.get(f"{YODLEE_API_BASE}/transactions", headers=headers)
        data = response.json()

        txns = data.get("transaction", [])
        if not txns:
            raise Exception("No transactions returned.")

        category_totals = {}
        total_spent = 0

        for txn in txns:
            category = txn.get("category", "Other").lower()
            amount = abs(txn.get("amount", 0))
            total_spent += amount
            category_totals[category] = category_totals.get(category, 0) + amount

        balance = income - total_spent

        return {
            "categories": category_totals,
            "total_spent": round(total_spent, 2),
            "balance": round(balance, 2)
        }

    except Exception as e:
        print(f"[Yodlee Error] {e}")

        category_ratios = {
            "food": 0.23,
            "shopping": 0.12,
            "subscriptions": 0.09,
            "housing": 0.45,
            "utilities": 0.11
        }

        category_totals = {cat: round(expenses * ratio, 2) for cat, ratio in category_ratios.items()}
        total_spent = round(sum(category_totals.values()), 2)
        balance = round(income - total_spent, 2)

        return {
            "categories": category_totals,
            "total_spent": total_spent,
            "balance": balance
        }
