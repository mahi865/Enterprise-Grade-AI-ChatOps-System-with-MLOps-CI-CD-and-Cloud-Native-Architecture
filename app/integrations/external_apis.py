import httpx

async def handle_external_apis(intent: str, message: str) -> dict:
    result = {}
    try:
        if intent.lower() == "bug":
            result["jira"] = await call_jira_api(message)
        elif intent.lower() == "sales":
            result["salesforce"] = await call_salesforce_api(message)
        elif intent.lower() == "support":
            result["zendesk"] = await call_zendesk_api(message)
    except Exception as e:
        print(f"[External API Handler] Error: {e}")
    return result

async def call_jira_api(message: str) -> dict:
    async with httpx.AsyncClient() as client:
        # Replace with real credentials and endpoint
        resp = await client.post("https://your-jira-instance/api", json={"summary": message})
        return resp.json()

async def call_salesforce_api(message: str) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.post("https://salesforce/api", json={"query": message})
        return resp.json()

async def call_zendesk_api(message: str) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.post("https://zendesk/api", json={"ticket": message})
        return resp.json()
