import base64

# https://developers.zoom.us/docs/integrations/oauth/
def test_base64():
    # For example, Client_ID:Client_Secret Base64-encoded is Q2xpZW50X0lEOkNsaWVudF9TZWNyZXQ=
    credentials = "Client_ID:Client_Secret"
    encode = base64.b64encode(credentials.encode()).decode()
    assert encode == "Q2xpZW50X0lEOkNsaWVudF9TZWNyZXQ="
