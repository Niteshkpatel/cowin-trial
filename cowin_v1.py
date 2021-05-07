import requests 
# from fake_useragent import UserAgent
from requests.exceptions import HTTPError
import logging
from datetime import datetime,timedelta


def _call_api(district_id,date):
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '^\\^',
            'sec-ch-ua-mobile': '?0',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'en-GB,en;q=0.9',
            'sec-gpc': '1',
            'If-None-Match': 'W/^\\^32b8-zP/J2L5iepOlr97I0UQuhoYaqb0^\\^',
        }

        params = (
            ('district_id', district_id),
            ('date', date),
        )

        response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict', headers=headers, params=params)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e

        return response.json()
dt = datetime.now()+timedelta(hours=5.5)
new_date = dt.strftime('%d-%m-%Y')
x = _call_api(district_id='448',date=new_date)
logging.warning('The msg is : %s'%str(x))