import pandas as pd
import mysql.connector
from mysql.connector import MySQLConnection, Error

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               port=3306,
                               database="derrick")

## ĐẨY DỮ LIỆU BẢNG CHAT
# df = pd.read_excel('D:\Python\convert\Chat_1212 .xlsx')
# cursor = mydb.cursor()
# # cursor.execute("USE derrick")
#
# for i, row in df.iterrows():
#     sql = "INSERT INTO chat (ngày,lượt_truy_cập,lượt_chat,lượt_truy_cập_có_chat,tỷ_lệ_truy_cập_có_chat,phản_hồi_chat,\
#           chat_chưa_phản_hồi,thời_gian_phản_hồi,tỷ_lệ_chuyển_đổi_yêu_cầu_phản_hồi,tỷ_lệ_phản_hồi_chat,\
#           người_mua,đơn_hàng,sản_phẩm,doanh_số_đ,tỷ_lệ_chuyển_đổi_phản_hồi_đơn_được_đặt)\
#           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#     val = (
#     row['ngày'], row['lượt_truy_cập'], row['lượt_chat'], row['lượt_truy_cập_có_chat'], row['tỷ_lệ_truy_cập_có_chat'],
#     row['phản_hồi_chat'], row['chat_chưa_phản_hồi'], row['thời_gian_phản_hồi'],
#     row['tỷ_lệ_chuyển_đổi_yêu_cầu_phản_hồi'],row['tỷ_lệ_phản_hồi_chat'], row['người_mua'], row['đơn_hàng'], row['sản_phẩm'],
#     row['doanh_số_đ'], row['tỷ_lệ_chuyển_đổi_phản_hồi_đơn_được_đặt'])
#     cursor.execute(sql, val)
#     # sql = "INSERT INTO chat (ngày,lượt_truy_cập,lượt_chat,thời_gian_phản_hồi,tỷ_lệ_truy_cập_có_chat) VALUES (%s,%s,%s,%s,%s)"
#     # val = (row['ngày'], row['lượt_truy_cập'], row['lượt_chat'], row['thời_gian_phản_hồi'], row['tỷ_lệ_truy_cập_có_chat'])
#     # cursor.execute(sql,val)
# mydb.commit()
# cursor.close()
# mydb.close()

### ĐẨY DỮ LIỆU BẲNG ORDER
# df = pd.read_excel('D:\Python\convert\parentskudetail_123.xlsx')
# cursor = mydb.cursor()
#
# for i, row in df.iterrows():
#     sql = "INSERT INTO orders (Sản_phẩm,Mã_sản_phẩm,Tên_Phân_Loại,Mã_phân_loại_hàng,SKU_phân_loại,SKU_sản_phẩm, \
#                   Lượt_truy_cập_sản_phẩm,Lượt_xem_trang_sản_phẩm,Số_lượng_khách_thoát_trang_sản_phẩm,Tỷ_lệ_thoát_Trang_sản_phẩm, \
#                   Lượt_click_từ_Trang_tìm_kiếm,Lượt_thích,Lượt_truy_cập_sản_phẩm_Thêm_vào_giỏ_hàng,Sản_phẩm_Thêm_vào_giỏ_hàng, \
#                   Tỷ_lệ_chuyển_đổi_theo_lượt_thêm_vào_giỏ_hàng,Người_mua_đã_đặt_hàng,Sản_phẩm_Đơn_đã_đặt,Doanh_số_Đơn_đã_đặt_VND, \
#                   Tỷ_lệ_chuyển_đổi_Đơn_đã_đặt,Người_mua_có_đơn_đã_xác_nhận,Sản_phẩm_Đơn_đã_xác_nhận,Doanh_số_Đơn_đã_xác_nhận_VND, \
#                   Tỷ_lệ_chuyển_đổi_Đơn_đã_xác_nhận,Tỷ_lệ_chuyển_đổi_Từ_Đơn_đã_đặt_thanh_Đơn_đã_xác_nhận)  \
#                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#     val = (
#                 row['Sản_phẩm'], row['Mã_sản_phẩm'], row['Tên_Phân_Loại'], row['Mã_phân_loại_hàng'], row['SKU_phân_loại'],
#                 row['SKU_sản_phẩm'], row['Lượt_truy_cập_sản_phẩm'], row['Lượt_xem_trang_sản_phẩm'],
#                 row['Số_lượng_khách_thoát_trang_sản_phẩm'], row['Tỷ_lệ_thoát_Trang_sản_phẩm'],
#                 row['Lượt_click_từ_Trang_tìm_kiếm'], row['Lượt_thích'], row['Lượt_truy_cập_sản_phẩm_Thêm_vào_giỏ_hàng'],
#                 row['Sản_phẩm_Thêm_vào_giỏ_hàng'], row['Tỷ_lệ_chuyển_đổi_theo_lượt_thêm_vào_giỏ_hàng'],
#                 row['Người_mua_đã_đặt_hàng'], row['Sản_phẩm_Đơn_đã_đặt'], row['Doanh_số_Đơn_đã_đặt_VND'],
#                 row['Tỷ_lệ_chuyển_đổi_Đơn_đã_đặt'], row['Người_mua_có_đơn_đã_xác_nhận'], row['Sản_phẩm_Đơn_đã_xác_nhận'],
#                 row['Doanh_số_Đơn_đã_xác_nhận_VND'], row['Tỷ_lệ_chuyển_đổi_Đơn_đã_xác_nhận'],
#                 row['Tỷ_lệ_chuyển_đổi_Từ_Đơn_đã_đặt_thanh_Đơn_đã_xác_nhận'],)
#     cursor.execute(sql,val)
# mydb.commit()
# cursor.close()
# mydb.close()

### ĐẨY DỮ LIỆU BẢNG PRODUCT OVERVIEW:
# df = pd.read_excel('D:\Python\convert\productoverview_123.xlsx')
# cursor = mydb.cursor()
#
# for i, row in df.iterrows():
#     sql = "INSERT INTO product_overview (Ngày,\
#           Lượt_truy_cập_sản_phẩm, \
#           Lượt_xem_trang_sản_phẩm, \
#           Sản_phẩm_được_truy_cập, \
#           Số_lượng_khách_thoát_trang_sản_phẩm, \
#           Tỷ_lệ_thoát_Trang_sản_phẩm, \
#           Lượt_click_từ_Trang_tìm_kiếm, \
#           Lượt_thích, \
#           Lượt_truy_cập_sản_phẩm_Thêm_vào_giỏ_hàng, \
#           Sản_phẩm_Thêm_vào_giỏ_hàng, \
#           Tỷ_lệ_chuyển_đổi_theo_lượt_thêm_vào_giỏ_hàng, \
#           Người_mua_đã_đặt_hàng, \
#           Sản_phẩm_Đơn_đã_đặt, \
#           Số_sản_phẩm_đã_bán, \
#           Doanh_số_Đơn_đã_đặt_VND, \
#           Tỷ_lệ_chuyển_đổi_Đơn_đã_đặt, \
#           Người_mua_có_đơn_đã_xác_nhận, \
#           Sản_phẩm_Đơn_đã_xác_nhận, \
#           Sản_phẩm_được_duyệt, \
#           Doanh_số_Đơn_đã_xác_nhận_VND, \
#           Tỷ_lệ_chuyển_đổi_Đơn_đã_xác_nhận, \
#           Tỷ_lệ_chuyển_đổi_Từ_Đơn_đã_đặt_thành_Đơn_đã_xác_nhận) \
#         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#     val = (
#         row['Ngày'],row['Lượt_truy_cập_sản_phẩm'], row['Lượt_xem_trang_sản_phẩm'], row['Sản_phẩm_được_truy_cập'],
#         row['Số_lượng_khách_thoát_trang_sản_phẩm'], row['Tỷ_lệ_thoát_Trang_sản_phẩm'],
#         row['Lượt_click_từ_Trang_tìm_kiếm'], row['Lượt_thích'], row['Lượt_truy_cập_sản_phẩm_Thêm_vào_giỏ_hàng'],
#         row['Sản_phẩm_Thêm_vào_giỏ_hàng'], row['Tỷ_lệ_chuyển_đổi_theo_lượt_thêm_vào_giỏ_hàng'],
#         row['Người_mua_đã_đặt_hàng'], row['Sản_phẩm_Đơn_đã_đặt'], row['Số_sản_phẩm_đã_bán'],
#         row['Doanh_số_Đơn_đã_đặt_VND'], row['Tỷ_lệ_chuyển_đổi_Đơn_đã_đặt'], row['Người_mua_có_đơn_đã_xác_nhận'],
#         row['Sản_phẩm_Đơn_đã_xác_nhận'], row['Sản_phẩm_được_duyệt'], row['Doanh_số_Đơn_đã_xác_nhận_VND'],
#         row['Tỷ_lệ_chuyển_đổi_Đơn_đã_xác_nhận'], row['Tỷ_lệ_chuyển_đổi_Từ_Đơn_đã_đặt_thành_Đơn_đã_xác_nhận'])
#     cursor.execute(sql, val)
# mydb.commit()
# cursor.close()
# mydb.close()

# from sqlalchemy import create_engine
# def get_connection():
#     return create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format('root','', 'localhost', 3306, 'derrick'))
#
# engine=get_connection()
#
# # Insert dữ liệu vào table
# df.to_sql('product_overview',engine, if_exists='replace', index=False)

### ĐẨY DỮ LIỆU BẢNG SALES
# df = pd.read_excel('D:\Python\convert\sales_overview_123.xlsx')
# cursor = mydb.cursor()
#
# for i, row in df.iterrows():
#     sql = "INSERT INTO sales (\
#           Ngày,\
#           Lượt_truy_cập,\
#           Khách_đã_đặt_hàng_chưa_thanh_toán,\
#           Sản_phẩm_khách_chưa_thanh_toán, \
#           Tất_cả_các_đơn, \
#           Doanh_số_Đơn_đã_đặt_VND, \
#           Tỷ_lệ_chuyển_đổi_Từ_Lượt_truy_cập_thành_Đơn_được_đặt, \
#           Người_mua_có_đơn_đã_xác_nhận,\
#           Sản_phẩm_Đơn_đã_xác_nhận,\
#           Đơn_đã_xác_nhận,\
#           Doanh_số_Đơn_đã_xác_nhận_VND,\
#           Doanh_số_trên_mỗi_Người_mua_Đơn_đã_xác_nhận_VND,\
#           Tỷ_lệ_chuyển_đổi,\
#           Tỷ_lệ_chuyển_đổi_Từ_Đơn_đã_đặt_thành_Đơn_đã_xác_nhận) \
#           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#     val = (
#         row['Ngày'], row['Lượt_truy_cập'], row['Khách_đã_đặt_hàng_chưa_thanh_toán'],
#         row['Sản_phẩm_khách_chưa_thanh_toán'], row['Tất_cả_các_đơn'], row['Doanh_số_Đơn_đã_đặt_VND'],
#         row['Tỷ_lệ_chuyển_đổi_Từ_Lượt_truy_cập_thành_Đơn_được_đặt'], row['Người_mua_có_đơn_đã_xác_nhận'],
#         row['Sản_phẩm_Đơn_đã_xác_nhận'], row['Đơn_đã_xác_nhận'], row['Doanh_số_Đơn_đã_xác_nhận_VND'], row['Doanh_số_trên_mỗi_Người_mua_Đơn_đã_xác_nhận_VND'],
#         row['Tỷ_lệ_chuyển_đổi'], row['Tỷ_lệ_chuyển_đổi_Từ_Đơn_đã_đặt_thành_Đơn_đã_xác_nhận'],)
#     cursor.execute(sql, val)
# mydb.commit()
# cursor.close()
# mydb.close()

# from sqlalchemy import create_engine
# def get_connection():
#     return create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format('root','', 'localhost', 3306, 'derrick'))
#
# engine=get_connection()
#
# # Insert dữ liệu vào table
# df.to_sql('sales',engine, if_exists='replace', index=False)

### ĐẨY BẢNG DỮ LIỆU TRAFFIC
# df = pd.read_excel('D:\Python\convert\Traffic_overview_123.xlsx')
# cursor = mydb.cursor()
#
# for i, row in df.iterrows():
#     sql = "INSERT INTO traffic_overview (\
#           Ngày,\
#           Lượt_xem,\
#           Số_lượt_xem_trung_bình,\
#           Thời_gian_xem_trung_bình,\
#           Tỉ_lệ_thoát_trang,\
#           Lượt_truy_cập,\
#           Số_khách_truy_cập_mới,\
#           Số_khách_truy_cập_hiện_tại,\
#           Người_theo_dõi_mới)\
#           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#     val = (
#         row['Ngày'], row['Lượt_xem'], row['Số_lượt_xem_trung_bình'], row['Thời_gian_xem_trung_bình'],
#         row['Tỉ_lệ_thoát_trang'], row['Lượt_truy_cập'],
#         row['Số_khách_truy_cập_mới'], row['Số_khách_truy_cập_hiện_tại'], row['Người_theo_dõi_mới'])
#     cursor.execute(sql, val)
# mydb.commit()
# cursor.close()
# mydb.close()

### ĐẨY DỮ LIỆU BẢNG DISCOUNT PROMOTION
# df = pd.read_excel('D:\Python\convert\discount_promotion_overview_123.xlsx')
# cursor = mydb.cursor()
#
# for i, row in df.iterrows():
#     sql = "INSERT INTO discount_promotion (\
#           Ngày_bắt_đầu,\
#           Ngày_kết_thúc,\
#           Doanh_số_VND,\
#           Đơn_hàng,\
#           Số_lượng_sản_phẩm_đã_bán,\
#           Người_mua,\
#           Doanh_số_trên_mỗi_Người_mua_VND) \
#           VALUES(%s,%s,%s,%s,%s,%s,%s)"
#     val = (
#         row['Ngày_bắt_đầu'], row['Ngày_kết_thúc'], row['Doanh_số_VND'], row['Đơn_hàng'],
#         row['Số_lượng_sản_phẩm_đã_bán'], row['Người_mua'], row['Doanh_số_trên_mỗi_Người_mua_VND'])
#     cursor.execute(sql, val)
# mydb.commit()
# cursor.close()
# mydb.close()


### Đẩy dữ liệu mobile
# df=pd.read_excel('D:\Python\convert\Traffic_overview_mobile.xlsx',sheet_name='Ứng dụng')
# from sqlalchemy import create_engine
# def get_connection():
#     return create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format('root','', 'localhost', 3306, 'derrick'))
#
# engine=get_connection()
#
# # Insert dữ liệu vào table
# df.to_sql('traffic_mobile',engine, if_exists='replace', index=False)

### Đẩy dữ liệu computer
# df=pd.read_excel('D:\Python\convert\Traffic_overview_computer.xlsx',sheet_name='Máy tính')
# from sqlalchemy import create_engine
# def get_connection():
#     return create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format('root','', 'localhost', 3306, 'derrick'))
#
# engine=get_connection()
#
# # Insert dữ liệu vào table
# df.to_sql('traffic_computer',engine, if_exists='replace', index=False)

### Đẩy dữ liệu orderall
# df=pd.read_excel('D:\DAF\cty\Order.all.1234.xlsx')
# from sqlalchemy import create_engine
# def get_connection():
#     return create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format('root','', 'localhost', 3306, 'derrick'))
#
# engine=get_connection()
#
# # Insert dữ liệu vào table
# df.to_sql('orders',engine, if_exists='append', index=False)
