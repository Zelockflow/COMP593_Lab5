import requests
DAD_JOKES_API_URL = 'https://icanhazdadjoke.com/'
DAD_JOKES_SEARCH_URL = f'{DAD_JOKES_API_URL}/search'

def main(): 
    joke = get_random_dad_joke()
    print(joke_list, sep='\n')
    return

def search_for_dad_jokes(search_term):
    """Gets a list of dad jokes that contain a search term
    """
    #setup the header paramaters
    header_params = {
        'accept': 'application/json'
    }
    
    #setup the query string parameters
    query_str_params = {
        'term': 
    }
    #Send the Get request to the Dad Jokes API
    print('Searching Dad Jokes API for "{search_term}" jokes...', end='')
    resp_msg = requests.get(DAD_JOKES_SEARCH_URL, headers=header_params, params=query_str_params)

    #Check whether the Get request was successful
    if resp_msg.ok:
        print('Success')
        body_dict = resp_msg.json()
        jokes_portion = body_dict['results']
        jokes_list = [j['joke'] for j ]
        return joke_dict['joke']
    else:
        print('Failed')
        print(f'Staus code: {resp_msg.status_code} ({resp_msg.reason})')

    return

def get_random_dad_joke():
    """Gets a random dad joke

    Returns:
        _type_: _description_
    """
    #setup the header paramaters
    header_params = {
        'accept': 'application/json'
    }
    #Send the Get request to the Dad Jokes API
    print('Sending GET request to Dad Jokes API...', end='')
    resp_msg = requests.post(DAD_JOKES_API_URL, headers=header_params)

    #Check whether the Get request was successful
    if resp_msg.ok:
        print('Success')
        joke_dict = resp_msg.json()
        return joke_dict['joke']
    else:
        print('Failed')
        print(f'Staus code: {resp_msg.status_code} ({resp_msg.reason})')

    return



if __name__ == '__main__':
    main()