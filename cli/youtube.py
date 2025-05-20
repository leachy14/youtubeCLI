import os
from typing import Dict, List

from google_auth_oauthlib.flow import InstalledAppFlow  # type: ignore[reportMissingImports]
from google.oauth2.credentials import Credentials  # type: ignore[reportMissingImports]
from googleapiclient.discovery import build  # type: ignore[reportMissingImports]

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
TOKEN_FILE = os.environ.get("YTX_TOKEN_FILE", "token.json")
CLIENT_SECRETS = os.environ.get("YTX_CLIENT_SECRETS", "client_secrets.json")


def authenticate() -> Credentials:
    """Perform OAuth device login and store credentials."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS, SCOPES)
        creds = flow.run_console()
        with open(TOKEN_FILE, "w", encoding="utf-8") as token:
            token.write(creds.to_json())
    return creds


def build_service(creds: Credentials | None = None):
    """Create the YouTube API client."""
    if creds is None:
        creds = authenticate()
    return build("youtube", "v3", credentials=creds)


def get_recommendations(service) -> List[Dict[str, str]]:
    """Return a list of recommended videos for the authenticated user."""
    response = (
        service.activities().list(part="snippet,contentDetails", home=True, maxResults=10).execute()
    )
    recommendations: List[Dict[str, str]] = []
    for item in response.get("items", []):
        snippet = item.get("snippet", {})
        details = item.get("contentDetails", {})
        video_id = details.get("upload", {}).get("videoId")
        if not video_id:
            continue
        recommendations.append(
            {
                "title": snippet.get("title", ""),
                "url": f"https://youtu.be/{video_id}",
            }
        )
    return recommendations
