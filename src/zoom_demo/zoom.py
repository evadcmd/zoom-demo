import base64

from pydantic import BaseModel

from zoom_demo import http
from zoom_demo.conf import secret

OAUTH_URL = "https://zoom.us/oauth/authorize"
TOKEN_URL = "https://zoom.us/oauth/token"
API_MEETING_URL = "https://api.zoom.us/v2/users/me/meetings"


class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str
    expires_in: int
    scope: str
    api_url: str


async def get_access_token(code: str) -> Token:
    payload = {
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": secret.redirect_uri,
    }
    credentials = f"{secret.client_id}:{secret.client_secret}"
    base64_credentials = base64.b64encode(credentials.encode()).decode()
    headers = {
        "Authorization": f"Basic {base64_credentials}",
    }
    status, data = await http.post(TOKEN_URL, headers, data=payload)
    if status == 200:
        return Token(**data)
    else:
        raise Exception(f"Error: {status}, {data}")


class Settings(BaseModel):
    host_video: bool
    participant_video: bool
    cn_meeting: bool
    in_meeting: bool
    join_before_host: bool
    jbh_time: int
    mute_upon_entry: bool
    watermark: bool
    use_pmi: bool
    approval_type: int
    audio: str
    auto_recording: str
    enforce_login: bool
    enforce_login_domains: str
    alternative_hosts: str
    alternative_host_update_polls: bool
    close_registration: bool
    show_share_button: bool
    allow_multiple_devices: bool
    registrants_confirmation_email: bool
    waiting_room: bool
    request_permission_to_unmute_participants: bool
    registrants_email_notification: bool
    meeting_authentication: bool
    encryption_type: str
    approved_or_denied_countries_or_regions: dict
    breakout_room: dict
    internal_meeting: bool
    continuous_meeting_chat: dict
    participant_focused_meeting: bool
    push_change_to_calendar: bool
    resources: list[any]
    alternative_hosts_email_notification: bool
    show_join_info: bool
    device_testing: bool
    focus_mode: bool
    meeting_invitees: list[any]
    private_meeting: bool
    email_notification: bool
    host_save_video_order: bool
    sign_language_interpretation: dict
    email_in_attendee_report: bool


class ZoomMeeting(BaseModel):
    uuid: str
    id: int
    host_id: str
    host_email: str
    topic: str
    type: int
    status: str
    start_time: str
    duration: int
    timezone: str
    created_at: str
    start_url: str
    join_url: str
    password: str
    h323_password: str
    pstn_password: str
    encrypted_password: str
    settings: Settings
    supportGoLive: bool
    creation_source: str
    pre_schedule: bool


async def create_meeting(token: str):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    meeting_data = {
        "topic": "topic",
        "type": 2,
        "start_time": "2024-12-25T10:00:00Z",
        "duration": 30,
        "timezone": "Asia/Tokyo",
        "settings": {"host_video": True, "participant_video": True},
    }
    status, data = await http.post(API_MEETING_URL, headers, json=meeting_data)
    if status == 201:
        return ZoomMeeting(**data)
    else:
        raise Exception(f"Error: {status}, {data}")
