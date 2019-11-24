"""File này chứa các hàm dùng cho việc phân loại bài post vào 3 nhóm:
- bài post hợp lệ
- bài post hợp lệ nhưng trùng lat, lng
- bài post không hợp lệ
"""
import numpy as np
import psycopg2

import app.settings as settings





def classify(post_info_dict):
    '''Phân loại bài post vào một trong 3 nhóm

    :Args:
    - post_info_dict - dict chứa attribute của bài post được gửi lên

    :Rets:
    - 0 - gửi thành công và bài post hợp lệ
    - 1 - gửi thành công và bài post không hợp lệ
    '''

    # Kiểm tra post có hợp lệ hay không
    # try:
    #     if post_info_dict['price_sell'] is None or post_info_dict['price_sell'] < 10000000:
    #         # send_error_post(post_info_dict)
    #         return 1

    #     if post_info_dict['area_cal'] is None or post_info_dict['area_cal'] <= 0:
    #         # send_error_post(post_info_dict)
    #         return 1

    #     if post_info_dict['lat'] is None:
    #         # send_error_post(post_info_dict)
    #         return 1

    #     if post_info_dict['realestate_type'] is None:
    #         # send_error_post(post_info_dict)
    #         return 1

    #     if post_info_dict['transaction_type'] is None:
    #         # send_error_post(post_info_dict)
    #         return 1
    # except Exception:
    #     # nếu có bất kì exception nào xảy ra, thì là do các phép so sánh xảy ra giữa kiểu float và kiểu None
    #     # tức là bài post đó không hợp lệ
    #     return 1


    # bổ sung trường `id`
    post_info_dict['id'] = 0

    # thêm nhiễu vào lat, lng
    if post_info_dict['lat']:
        post_info_dict['lat'] += np.random.uniform(-0.0005, 0.0005)
        post_info_dict['long'] += np.random.uniform(-0.0005, 0.0005)
        # bổ sung 2 trường là 'coordinate'
        post_info_dict['coordinate'] = f"point({post_info_dict['long']},{post_info_dict['lat']})"
    else:
        post_info_dict['coordinate'] = "point(null,null)"

    return send_post(post_info_dict)


# this order is for testing
# SENDING_ATTRIBUTE_ORDER = [
#     'page_source',
#     'link',
#     'title',
#     'content',
#     'address_street',
#     'address_ward',
#     'surrounding',
#     'surrounding_name',
#     'surrounding_characteristics',
#     'area_cal',
#     'interior_room',
#     'project',
#     'address_city',
#     'address_district',
#     'post_date',
#     'crawled_date',
#     'transaction_type',
#     'realestate_type',
#     'price_sell',
#     'price_rent',
#     'legal',
#     'floor',
#     'position_street',
#     'potential',
#     'area_origin',
#     'address_number',
#     'lat',
#     'long',
#     'coordinate',
#     'post_id',
#     'price_m2',
#     'orientation'
# ]

SENDING_ATTRIBUTE_ORDER = [
    'page_source',
    'link',
    'title',
    'content',
    'address_street',
    'address_ward',
    'surrounding',
    'surrounding_name',
    'surrounding_characteristics',
    'interior_room',
    'project',
    'address_city',
    'address_district',
    'transaction_type',
    'realestate_type',
    'price_sell',
    'price_rent',
    'legal',
    'floor',
    'position_street',
    'potential',
    'area_origin',
    'address_number',
    'lat',
    'long',
    'coordinate',
    'price_m2',
    'orientation',
    'area_cal',
    'post_id',
    'post_date',
    'crawled_date',
]


def send_post(post_info_dict):
    '''Gửi bài post lên table 'post' trong DB 'sharklanddb'
    '''

    isErr = False

    if post_info_dict is None:
        return "Internal error"

    try:
        connection = psycopg2.connect(
            user      = settings.POSTGRE_USER,
            password  = settings.POSTGRE_PASS,
            host      = settings.POSTGRE_HOST,
            port      = settings.POSTGRE_PORT,
            database  = settings.POSTGRE_DB,
            options   = f'-c search_path={settings.POSTGRE_SCHEM}')

        cursor = connection.cursor()

        send_data = 'default'
        for attr in SENDING_ATTRIBUTE_ORDER:
            if attr in ["content", 'link', 'title', 'post_id', 'interior_room', 'orientation',
                        'address_street', 'address_ward', 'surrounding', 'surrounding_name',
                        'surrounding_characteristics', 'project'
                        ]:
                tmp = "'" + str(post_info_dict[attr]) + "'" if post_info_dict[attr] is not None else "null"
            elif attr in ['potential', 'area_origin']:
                tmp = "array["
                for i, val in enumerate(post_info_dict[attr]):
                    tmp += str(val)
                    if i < len(post_info_dict[attr]) - 1:
                        tmp += ','
                tmp += ']'

            elif attr == 'realestate_type':
                if post_info_dict[attr] == 0 or ~isinstance(post_info_dict[attr], int):
                    tmp = '6'
                else:
                    tmp = str(post_info_dict[attr])

            elif post_info_dict[attr] is None:
                tmp = 'null'
            elif ~isinstance(post_info_dict[attr], str):
                tmp = str(post_info_dict[attr])
            else:
                tmp = post_info_dict[attr]

            send_data = send_data + ',' + tmp

        cursor.execute(f"INSERT INTO {settings.POSTGRE_TABLE}(id, page_source, link, title, content, address_street, address_ward, surrounding, surrounding_name, surrounding_characteristics, interior_room, project, address_city, address_district, transaction_type, realestate_type, price_sell, price_rent, legal, floor, position_street, potential, area_origin, address_number, lat, long, coordinate, price_m2, orientation, area_cal, post_id, post_date, crawled_date) VALUES ({send_data});")
        connection.commit()

    except (psycopg2.Error) as error :
        print("Error while connecting to PostgreSQL: ", error)
        isErr = True
    finally:
        if (connection):
            cursor.close()
            connection.close()

    if isErr:
        return "Internal error."
    else:
        return "OK"
