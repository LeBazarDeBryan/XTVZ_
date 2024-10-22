import requests
import json
import urllib.parse

# Informations d'authentification
USERNAME = os.environ.get('TF1_USER')
PASSWORD = os.environ.get('TF1_PASSWORD')
USER_AGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like MacOS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
group_name = "TF1 Plus"

# URL et clés d'API
TF1_DIRECT_URL = "https://www.tf1.fr/direct"
AUTH_URL = "https://compte.tf1.fr/accounts.login"
SESSION_URL = "https://www.tf1.fr/token/gigya/web"
GIGYA_API_KEY = requests.get(TF1_DIRECT_URL).text.split('gigya":{"apiKey":"')[1].split('"')[0]
GRAPHQL_URL = "https://www.tf1.fr/graphql/web"
GRAPHQL_ID = "ecf53113697d74c6a7771ad8ed018b5a22ae7a06"

def login(username, password):
    payload = {
        "loginID": username,
        "password": password,
        "APIKey": GIGYA_API_KEY,
        "includeUserInfo": "true"
    }
    headers = {
        "Referer": TF1_DIRECT_URL,
        "User-Agent": USER_AGENT
    }
    res = requests.post(AUTH_URL, data=payload, headers=headers)
    res_json = res.json()
    
    if res_json.get('statusCode') == 200:
        uid = res_json['userInfo']['UID']
        signature = res_json['userInfo']['UIDSignature']
        timestamp = res_json['userInfo']['signatureTimestamp']
        session_payload = {
            "uid": uid,
            "signature": signature,
            "timestamp": timestamp,
            "consent_ids": ["1", "2", "3", "4", "10001", "10003", "10005", "10007", "10013", "10015", "10017", "10019", "10009", "10011", "13002", "13001", "10004", "10014", "10016", "10018", "10020", "10010", "10012", "10006", "10008"]
        }
        session_res = requests.post(SESSION_URL, json=session_payload)
        session_res_json = session_res.json()
        if session_res_json.get('right') == "BASIC":
            user_token = session_res_json['token']
            return user_token
    return None

def json_encode(data):
    return urllib.parse.quote(json.dumps(data))

def get_channel_list():
    graphql_query = json_encode({"ofChannelTypes": ["DIGITAL", "TV", "EVENT"], "limit": 500})
    encoded_url = f"{GRAPHQL_URL}?id={GRAPHQL_ID}&variables={graphql_query}"
    response = requests.get(encoded_url)
    channel_list = response.json()['data']['lives']['items']
    return [
        (
            item['channel']['live']['streamId'], 
            item['channel']['slug'], 
            item['channel']['thematic']['slug'], 
            item['channel']['thematic']['label'], 
            item['channel']['id'], 
            item['channel']['type'], 
            item['channel']['decoration']['logo']['sourcesWithScales'][0]['url'], 
            item['channel']['label']
        ) for item in channel_list
    ]

def get_hls_urls(channel_id, user_token):
    URL_API = f"https://mediainfo.tf1.fr/mediainfocombo/{channel_id}?pver=5015000&format=hls"
    headers = {
        "User-Agent": USER_AGENT,
        "authorization": f"Bearer {user_token}"
    }
    api_response = requests.get(URL_API, headers=headers)
    api_response_json = api_response.json()
    if api_response_json.get('delivery', {}).get('code') == "200":
        hls_url = api_response_json['delivery']['url']
        if hls_url.endswith("hls-sd.m3u8"):
            hls_url = hls_url.replace("hls-sd.m3u8", "hls-hd.m3u8")
        return hls_url
    return None

def build_playlist(group_option="thematic"):
    user_token = login(USERNAME, PASSWORD)
    if not user_token:
        print("Échec de l'authentification. Vérifiez votre nom d'utilisateur et votre mot de passe.")
        return
    
    channel_list = get_channel_list()
    
    for stream_id, slug, thematic_slug, thematic_label, id_, type_, logo, label in channel_list:
        channel_id = stream_id.strip('"')
        clean_name = label.replace(',', '').replace('"', '')
        if group_option == "thematic":
            m3u_group_name = thematic_label
        else:
            m3u_group_name = group_name
        print(f'#EXTINF:-1 tvg-name="{clean_name}" tvg-logo={logo} group-title={m3u_group_name},{clean_name}')
        hls_url = get_hls_urls(channel_id, user_token)
        if hls_url:
            print(hls_url)
        else:
            print("Chaîne non trouvée dans la liste.")

if __name__ == "__main__":
    build_playlist()
