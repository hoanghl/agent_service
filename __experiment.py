from app.modules.classify import send_post

post_info = {
    "address_city": 1,
    "address_district": 13,
    "address_number": None,
    "address_street": "Đông Hưng Thuận 9",
    "address_ward": " đông hưng thuận",
    "area_cal": 100.0,
    "area_origin": [
        0,
        0
    ],
    "content": "Đất quận 12 phía sau chợ An Sương bán nhanh để thu hồi vốn bung ra bán ai đến sớm được hỗ trợ sản phẩm tốt giá đẹp. Còn 8 lô tái định cư giá rớt cọc (20 nền nhưng chỉ còn 8 nền). Giá chỉ từ 15,8tr/m2 sổ hồng tại công ty, sang tên công chứng trong ngày, xây dựng tự do. Liên hệ ngay : 0971649767 Em Thanh có Zalo \n Địa chỉ: Đông Hưng Thuận 9, Phường Đông Hưng Thuận, Quận 12, TP.HCM",
    "floor": 1,
    "interior_room": None,
    "legal": 3,
    "lat": 10.42332423,
    "long": 108.42534523,
    "orientation": None,
    "page_source": 2,
    "position_street": None,
    "potential": [
        2
    ],
    "price_m2": 15800000,
    "price_rent": 0,
    "price_sell": 15800000,
    "project": None,
    "realestate_type": 1,
    "surrounding": "chợ",
    "surrounding_characteristics": None,
    "surrounding_name": "chợ An Sương",
    "transaction_type": 1,
    "link" : "https://",
    "title" : "No title at all",
    "post_id" : "32",
    "post_date": 432423423,
    "crawled_date": 4324237733,
    'coordinate' : "point(108.42534523,10.42332423)"
}

send_post(post_info)
