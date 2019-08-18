import requests, hashlib, os, logging
from lxml import etree
from fake_useragent import UserAgent

logging.basicConfig(filename="/var/www/namephoto/touxiang/shiyan.txt", filemode="a",
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%Y-%m-%d %H:%M:%S",
                    level=logging.DEBUG)

path = "/home/photo/"
files = os.listdir(path)
for l in range(400):
    logging.debug("第{}页".format(l))
    for i in range(1, 3):
        for k in range(1, 10):
            u_a = UserAgent().random


            def headers():
                # 配置请求头
                header = {
                    "User-Agent": "{}".format(u_a),
                }
                return header


            try:
                photo_list = requests.get("https://www.gexing.com/qqtouxiang/new/{}".format(l), headers=headers())
                response = photo_list.content.decode()
                html = etree.HTML(response)
                big_photo = html.xpath('//*[@id="tx_post_list"]/ul[{}]/li[{}]/div[1]/a/@href'.format(i, k))
                num = str(big_photo[0])
                number = num.strip("https://www.gexing.com/qqtouxiang/")
                number = number.strip(".html")
                print(number)
                name = requests.get(big_photo[0], headers=headers())
                p = name.content.decode()
                md5 = hashlib.md5()
            except Exception as e:
                logging.debug("这是第一条报错信息::::::{}".format(e))

            try:
                for j in range(1, 31):
                    if j < 10:
                        html = etree.HTML(p)
                        photo = html.xpath('//*[@id="119087{}{}"]/img/@src'.format(number, j))
                        if photo:
                            da = requests.get(photo[0], headers=headers())
                            da = da.content
                            md5.update(da)
                            name1 = md5.hexdigest()
                            name = 'photo{}.jpeg'.format(name1)
                            if name not in files:
                                with open('/home/photo2/photo{}.jpg'.format(name1), 'wb') as f:
                                    f.write(da)
                            else:
                                ...
                        else:
                            break
                    if 9 < j < 22:
                        photo_2 = requests.get('https://www.gexing.com/qqtouxiang/{}_2.html'.format(number),
                                               headers=headers())
                        photo_2 = photo_2.content.decode()
                        html = etree.HTML(photo_2)
                        photo_2 = html.xpath('//*[@id="119087{}{}"]/img/@src'.format(number, j))
                        if photo_2:
                            da = requests.get(photo_2[0], headers=headers())
                            da = da.content
                            md5.update(da)
                            name1 = md5.hexdigest()
                            name = 'photo{}.jpeg'.format(name1)
                            if name not in files:
                                with open('/home/photo2/photo{}.jpg'.format(name1), 'wb') as f:
                                    f.write(da)
                            else:
                                ...
                        else:
                            break
                    elif j > 21:
                        photo_3 = requests.get('https://www.gexing.com/qqtouxiang/{}_3.html'.format(number),
                                               headers=headers())
                        photo_3 = photo_3.content.decode()
                        html = etree.HTML(photo_3)
                        photo_3 = html.xpath('//*[@id="119087{}{}"]/img/@src'.format(number, j))
                        if photo_3:
                            da = requests.get(photo_3[0], headers=headers())
                            da = da.content
                            md5.update(da)
                            name1 = md5.hexdigest()
                            name = 'photo{}.jpeg'.format(name1)
                            if name not in files:
                                with open('/home/photo2/photo{}.jpg'.format(name1), 'wb') as f:
                                    f.write(da)
                            else:
                                ...
                        else:
                            continue
            except Exception as e:
                logging.debug("这是第二条报错信息:::{}".format(e))
