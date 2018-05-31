import requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing


def simple_get(url):
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'ExcellentRentz'
        }
    )

    try:
        with closing(get(url, stream=True, headers=headers)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return log_error(resp.content)

    except RequestException as e:
        log_error('Hemmagjord Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
	content_type = resp.headers['Content-Type'].lower()
	return (resp.status_code == 200
		and content_type is not None 
		and content_type.find('html') > -1)


def log_error(e): 
	print(e)