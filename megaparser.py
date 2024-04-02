import tls_client
from time import sleep
import random


def parser_mega(delivery_type, min_price, max_price, search_query, min_precent_bonus, link_id, proxy_str):

    client_identifier_list = ['chrome_103', 'chrome_104', 'chrome_105', 'chrome_106', 'chrome_107', 'chrome_108', 'chrome109', 'Chrome110', 'chrome111', 'chrome112', 'chrome_116_PSK', 'chrome_116_PSK_PQ', 'chrome_117', 'chrome_120', 'firefox_102', 'firefox_104', 'firefox108', 'Firefox110', 'firefox_117', 'firefox_120', 'opera_89', 'opera_90', 'safari_15_3', 'safari_15_6_1', 'safari_16_0', 'safari_ios_15_5', 'safari_ios_15_6', 'safari_ios_16_0', 'safari_ios_15_6', 'okhttp4_android_7', 'okhttp4_android_8', 'okhttp4_android_9', 'okhttp4_android_10', 'okhttp4_android_11', 'okhttp4_android_12', 'okhttp4_android_13']
    for client_str in client_identifier_list:
        session = tls_client.Session(
            client_identifier=client_str,
            random_tls_extension_order=True
        )

        cookies = {
            'spid': '1691248327816_541d895417a4ec2f5cad563effefd88c_o92886xo5rqsjwsc',
            '_ym_uid': '1691248329912430874',
            '_ym_d': '1691248329',
            '_ym_isad': '1',
            'megaCookiesMigrated': 'true',
            'device_id': '7274abde-33a2-11ee-8527-0242ac110003',
            'sbermegamarket_token': 'ec419949-e34c-470f-9786-d7c59548a057',
            'ecom_token': 'ec419949-e34c-470f-9786-d7c59548a057',
            'ssaid': '737ceeb0-33a2-11ee-b522-155d36424484',
            'adspire_uid': 'AS.113553684.1691248331',
            'isOldUser': 'true',
            'tmr_lvid': '55347914a83053f236fe7053e560ce89',
            'tmr_lvidTS': '1691248331311',
            'adtech_uid': 'f47d1ae8-a1cd-4296-a757-7f26ae75c1a9%3Amegamarket.ru',
            'top100_id': 't1.6795753.1618216597.1691248331476',
            '_sa': 'SA1.cd4985e3-ee50-447e-828a-fdd84528ca14.1691248332',
            '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"10002472"}',
            'rrpvid': '513614847305501',
            '_gid': 'GA1.2.1410320537.1691248337',
            '_gcl_au': '1.1.3998593.1691248337',
            'flocktory-uuid': '4848fa36-60eb-4f39-89ed-ec9f4240cb0f-7',
            'rcuid': '64cbbc0b31740866e0fdfcc9',
            'uxs_uid': '777ea0d0-33a2-11ee-ba92-57f9b962517d',
            'viewType': 'grid',
            'spsc': '1691302154596_2cd4bb1047e6a64ffaffdec07486904a_a5476469b72f558bb72e6aae99c6a060',
            '_ym_visorc': 'b',
            '__zzatw-smm': 'MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2UbN1ddHBEkWA4hPwsXXFU+NVQOPHVXLw0uOF4tbx5lUFoiQ1dOfi4fE3lnFRtQSxgvS18+bX0yUCs5Lmw=KeUgyQ==',
            'last_visit': '1691284159771%3A%3A1691302159771',
            'tmr_detect': '1%7C1691302159796',
            'region_info': '%7B%22displayName%22%3A%22%D0%91%D0%90%D0%A8%D0%9A%D0%9E%D0%A0%D0%A2%D0%9E%D0%A1%D0%A2%D0%90%D0%9D%20%D0%A0%D0%95%D0%A1%D0%9F%D0%A3%D0%91%D0%9B%D0%98%D0%9A%D0%90%22%2C%22kladrId%22%3A%220200000000000%22%2C%22isDeliveryEnabled%22%3Atrue%2C%22geo%22%3A%7B%22lat%22%3A54.736202%2C%22lon%22%3A55.958057%7D%2C%22id%22%3A%2202%22%7D',
            '_gat': '1',
            't3_sid_6795753': 's1.524378982.1691302155053.1691302215798.3.16',
            'cfidsw-smm': 'CmgFYMcct7IyHeDYhhxqzsz5N+WFHF1M1Al0Qbyn2cBzoTVfDldDVHByn0VRJDGXoRimSOX202cpEQcU0AsIKmg377LGcZU+RaWZhcSJri5jB9cyFEga1w2ymZKeONPSL7azAjdDPzJ2S3bHZKIwklselZJ5coNp1MbIrRE=',
            'cfidsw-smm': 'CmgFYMcct7IyHeDYhhxqzsz5N+WFHF1M1Al0Qbyn2cBzoTVfDldDVHByn0VRJDGXoRimSOX202cpEQcU0AsIKmg377LGcZU+RaWZhcSJri5jB9cyFEga1w2ymZKeONPSL7azAjdDPzJ2S3bHZKIwklselZJ5coNp1MbIrRE=',
            '__tld__': 'null',
            '_ga': 'GA1.1.1664009550.1691248331',
            '_ga_W49D2LL5S1': 'GS1.1.1691302156.5.1.1691302217.60.0.0',
        }

        headers = {
            'authority': 'megamarket.ru',
            'accept': 'application/json',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            # 'cookie': 'spid=1691248327816_541d895417a4ec2f5cad563effefd88c_o92886xo5rqsjwsc; _ym_uid=1691248329912430874; _ym_d=1691248329; _ym_isad=1; megaCookiesMigrated=true; device_id=7274abde-33a2-11ee-8527-0242ac110003; sbermegamarket_token=ec419949-e34c-470f-9786-d7c59548a057; ecom_token=ec419949-e34c-470f-9786-d7c59548a057; ssaid=737ceeb0-33a2-11ee-b522-155d36424484; adspire_uid=AS.113553684.1691248331; isOldUser=true; tmr_lvid=55347914a83053f236fe7053e560ce89; tmr_lvidTS=1691248331311; adtech_uid=f47d1ae8-a1cd-4296-a757-7f26ae75c1a9%3Amegamarket.ru; top100_id=t1.6795753.1618216597.1691248331476; _sa=SA1.cd4985e3-ee50-447e-828a-fdd84528ca14.1691248332; _gpVisits={"isFirstVisitDomain":true,"idContainer":"10002472"}; rrpvid=513614847305501; _gid=GA1.2.1410320537.1691248337; _gcl_au=1.1.3998593.1691248337; flocktory-uuid=4848fa36-60eb-4f39-89ed-ec9f4240cb0f-7; rcuid=64cbbc0b31740866e0fdfcc9; uxs_uid=777ea0d0-33a2-11ee-ba92-57f9b962517d; viewType=grid; spsc=1691302154596_2cd4bb1047e6a64ffaffdec07486904a_a5476469b72f558bb72e6aae99c6a060; _ym_visorc=b; __zzatw-smm=MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2UbN1ddHBEkWA4hPwsXXFU+NVQOPHVXLw0uOF4tbx5lUFoiQ1dOfi4fE3lnFRtQSxgvS18+bX0yUCs5Lmw=KeUgyQ==; last_visit=1691284159771%3A%3A1691302159771; tmr_detect=1%7C1691302159796; region_info=%7B%22displayName%22%3A%22%D0%91%D0%90%D0%A8%D0%9A%D0%9E%D0%A0%D0%A2%D0%9E%D0%A1%D0%A2%D0%90%D0%9D%20%D0%A0%D0%95%D0%A1%D0%9F%D0%A3%D0%91%D0%9B%D0%98%D0%9A%D0%90%22%2C%22kladrId%22%3A%220200000000000%22%2C%22isDeliveryEnabled%22%3Atrue%2C%22geo%22%3A%7B%22lat%22%3A54.736202%2C%22lon%22%3A55.958057%7D%2C%22id%22%3A%2202%22%7D; _gat=1; t3_sid_6795753=s1.524378982.1691302155053.1691302215798.3.16; cfidsw-smm=CmgFYMcct7IyHeDYhhxqzsz5N+WFHF1M1Al0Qbyn2cBzoTVfDldDVHByn0VRJDGXoRimSOX202cpEQcU0AsIKmg377LGcZU+RaWZhcSJri5jB9cyFEga1w2ymZKeONPSL7azAjdDPzJ2S3bHZKIwklselZJ5coNp1MbIrRE=; cfidsw-smm=CmgFYMcct7IyHeDYhhxqzsz5N+WFHF1M1Al0Qbyn2cBzoTVfDldDVHByn0VRJDGXoRimSOX202cpEQcU0AsIKmg377LGcZU+RaWZhcSJri5jB9cyFEga1w2ymZKeONPSL7azAjdDPzJ2S3bHZKIwklselZJ5coNp1MbIrRE=; __tld__=null; _ga=GA1.1.1664009550.1691248331; _ga_W49D2LL5S1=GS1.1.1691302156.5.1.1691302217.60.0.0',
            'origin': 'https://megamarket.ru',
            'referer': 'https://megamarket.ru/catalog/',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }


        if link_id is not None:
            list_goods = []
            page = 0
            while page != 112 and page < 112:
                json_data = {
                    'selectedAssumedCollectionId': str(link_id), #ID Категории дубль
                    'collectionId': str(link_id), #ID Категории
                    'requestVersion': 10,
                    'limit': 44,
                    'offset': page,
                    'isMultiCategorySearch': False,
                    'searchByOriginalQuery': False,
                    'selectedSuggestParams': [],
                    'expandedFiltersIds': [],
                    'sorting': 1, #Фильтр от самых дешевых
                    'ageMore18': None,
                    'addressId': '8b153339-bc32-4948-b917-9588db7ace58#10#',
                    'showNotAvailable': True,
                    'selectedFilters': [
                        {
                            'filterId': 'OFFER_DUE_DATE_FILTER',
                            'type': 0,
                            'value': str(delivery_type), #Доставка
                        },
                        {
                            'filterId': '88C83F68482F447C9F4E401955196697',
                            'type': 1,
                            'value': str(min_price), #Минимальная цена
                        },
                        {
                            'filterId': '88C83F68482F447C9F4E401955196697',
                            'type': 2,
                            'value': str(max_price), #Максимальная цена
                        },
                    ],
                    'auth': {
                        'locationId': '63',
                        'appPlatform': 'WEB',
                        'appVersion': 0,
                        'experiments': {
                            '8': '2',
                            '55': '2',
                            '58': '2',
                            '62': '1',
                            '68': '2',
                            '69': '1',
                            '79': '3',
                            '84': '2',
                            '96': '2',
                            '98': '1',
                            '99': '1',
                            '107': '2',
                            '109': '2',
                            '119': '1',
                            '120': '2',
                            '121': '2',
                            '122': '1',
                            '126': '1',
                            '128': '1',
                            '130': '1',
                            '132': '1',
                            '144': '3',
                            '147': '3',
                            '154': '1',
                            '163': '2',
                            '178': '1',
                            '184': '3',
                            '186': '1',
                            '190': '2',
                            '192': '2',
                            '200': '2',
                            '205': '2',
                            '209': '1',
                            '218': '1',
                            '228': '2',
                            '229': '2',
                            '235': '2',
                            '237': '2',
                            '243': '1',
                            '255': '2',
                            '644': '3',
                            '645': '2',
                            '723': '2',
                            '772': '1',
                            '5779': '2',
                            '20121': '1',
                            '70070': '2',
                            '85160': '2',
                            '123999': '1',
                            '89898989': '1',
                        },
                        'os': 'UNKNOWN_OS',
                    },
                }
                response = session.post(
                'https://megamarket.ru/api/mobile/v1/catalogService/catalog/search',
                cookies=cookies,
                headers=headers,
                json=json_data,
                proxy=f'http://{proxy_str}'
                ).json()
                
                
                for i in range(44):
                    try:
                        tovar_price = response['items'][i]['price']
                        tovar_bonus_precent = response['items'][i]['bonusPercent']
                        tovar_bonus_count = response['items'][i]['bonusAmount']
                        tovar_name = response['items'][i]['goods']['title']
                        try:
                            tovar_seller = response['items'][i]['favoriteOffer']['merchantName']
                        except:
                            tovar_seller = 'err'
                        try:
                            tovar_link = response['items'][i]['goods']['webUrl']
                        except:
                            tovar_link = 'err'
                        try:
                            tovar_image = response['items'][i]['goods']['titleImage']
                        except:
                            tovar_image = 'err'
                        if int(tovar_bonus_precent) >= int(min_precent_bonus):
                            list_goods.append([tovar_price, tovar_bonus_precent, tovar_bonus_count, tovar_seller, tovar_link, tovar_image, tovar_name])
                    except:
                        pass
                page += 28
            return list_goods



        elif search_query is not None:
            list_goods = []
            page = 0
            while page != 112 and page < 112:
                json_data = {
                    'requestVersion': 10,
                    'limit': 44,
                    'offset': page,
                    'isMultiCategorySearch': False,
                    'searchByOriginalQuery': False,
                    'selectedSuggestParams': [],
                    'expandedFiltersIds': [],
                    'sorting': 1, #Фильтр от самых дешевых
                    'ageMore18': None,
                    'addressId': '8b153339-bc32-4948-b917-9588db7ace58#10#',
                    'showNotAvailable': True,
                    'selectedFilters': [
                        {
                            'filterId': 'OFFER_DUE_DATE_FILTER',
                            'type': 0,
                            'value': str(delivery_type), #Доставка
                        },
                        {
                            'filterId': '88C83F68482F447C9F4E401955196697',
                            'type': 1,
                            'value': str(min_price), #Минимальная цена
                        },
                        {
                            'filterId': '88C83F68482F447C9F4E401955196697',
                            'type': 2,
                            'value': str(max_price), #Максимальная цена
                        },
                    ],
                    'searchText': str(search_query), #Поисковый запрос
                    'auth': {
                        'locationId': '63',
                        'appPlatform': 'WEB',
                        'appVersion': 0,
                        'experiments': {
                            '8': '2',
                            '55': '2',
                            '58': '2',
                            '62': '1',
                            '68': '2',
                            '69': '1',
                            '79': '3',
                            '84': '2',
                            '96': '2',
                            '98': '1',
                            '99': '1',
                            '107': '2',
                            '109': '2',
                            '119': '1',
                            '120': '2',
                            '121': '2',
                            '122': '1',
                            '126': '1',
                            '128': '1',
                            '130': '1',
                            '132': '1',
                            '144': '3',
                            '147': '3',
                            '154': '1',
                            '163': '2',
                            '178': '1',
                            '184': '3',
                            '186': '1',
                            '190': '2',
                            '192': '2',
                            '200': '2',
                            '205': '2',
                            '209': '1',
                            '218': '1',
                            '228': '2',
                            '229': '2',
                            '235': '2',
                            '237': '2',
                            '243': '1',
                            '255': '2',
                            '644': '3',
                            '645': '2',
                            '723': '2',
                            '772': '1',
                            '5779': '2',
                            '20121': '1',
                            '70070': '2',
                            '85160': '2',
                            '123999': '1',
                            '89898989': '1',
                        },
                        'os': 'UNKNOWN_OS',
                    },
                }
                response = session.post(
                    'https://megamarket.ru/api/mobile/v1/catalogService/catalog/search',
                    cookies=cookies,
                    headers=headers,
                    json=json_data,
                    proxy=f'http://{proxy_str}'
                ).json()

                for i in range(44):
                    try:
                        tovar_price = response['items'][i]['price']
                        tovar_bonus_precent = response['items'][i]['bonusPercent']
                        tovar_bonus_count = response['items'][i]['bonusAmount']
                        tovar_name = response['items'][i]['goods']['title']
                        try:
                            tovar_seller = response['items'][i]['favoriteOffer']['merchantName']
                        except:
                            tovar_seller = 'err'
                        try:
                            tovar_link = response['items'][i]['goods']['webUrl']
                        except:
                            tovar_link = 'err'
                        try:
                            tovar_image = response['items'][i]['goods']['titleImage']
                        except:
                            tovar_image = 'err'
                        if int(tovar_bonus_precent) >= int(min_precent_bonus):
                            list_goods.append([tovar_price, tovar_bonus_precent, tovar_bonus_count, tovar_seller, tovar_link, tovar_image, tovar_name])
                    except:
                        pass
                page += 28
            return list_goods


    