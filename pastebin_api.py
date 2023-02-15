import requests

DEVELOPER_KEY = 'w-1zT2V4vhy-SFwxQuy--g5gap1vBU1h'
PASTEBIN_API_URL = 'https://pastebin.com/api/api_post.php'

def main(): 
    
    url = post_new_paste('This is a tittle','this is the body')
    print(f'new paste URL: {url}')

def post_new_paste(title, body_text, expiration='10M', listed=False):
    """Posts a new public paste to PasteBin

    Args:
        title (str): paste tietle
        body_text (str): Paste body text
        expiration (str, optional): Expiration date of paste(N = never 10M = minutes, 1H, 1D, 1W,2W,1M,6M,1Y) Default
        listed (bool, optional): Whether paste is publicly listed (true) or not (False). Defaults to False.

    Returns:
        str: URL of the new paste, if succeful. None unsuccessful.
    """
    paste_params = {
        'api_dev_key': DEVELOPER_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if listed else 1

    }
    resp_msg = requests.post(PASTEBIN_API_URL, data=paste_params)

    if resp_msg.ok:
        print('Success')
        return resp_msg.text
    else:
        print('Failed')
        print(f'Staus code: {resp_msg.status_code} ({resp_msg.reason})')
    return

if __name__ == '__main__':
    main()