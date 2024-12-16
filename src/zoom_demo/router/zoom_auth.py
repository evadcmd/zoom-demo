from fastapi import APIRouter
from zoom_demo.conf import secret
from zoom_demo import zoom
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode


router = APIRouter(prefix="/zoom-auth", tags=["zoom-auth"])


@router.get(path="")
async def zoom_auth(code: str | None = None):
    if code:
        # we can cache the token to avoid requesting a new one as long as the current token has not expired
        token = await zoom.get_access_token(code)
        meeting = await zoom.create_meeting(token.access_token)
        # keep it simple for the demo
        return {
            "start_url": meeting.start_url,
            "join_url": meeting.join_url,
        }
    else:
        return RedirectResponse(
            url=f"{zoom.OAUTH_URL}?{urlencode({
            "response_type": "code",
            "client_id": secret.client_id,
            "redirect_uri": secret.redirect_url
        })}"
        )
