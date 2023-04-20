import pandas as pd

def convert_chuoi(a):
    return a.replace('-', '')


def convert_per(a):
    return a.str.replace(',', '').str.replace('%', '').astype('float') / 100


def convert_int(a):
    return a.str.replace('.', '').astype('int')/100

def convert_weight(a):
    return a.replace('.','').astype('float')

def convert_money(a):
    return a.replace('.', '').astype('int')

### Cleaning data table 'DETAIL'
df=pd.read_excel('D:\Python\convert\parentskudetail_123.xlsx')

# replace space = _
df.columns = df.columns.str.replace(' ', '_').str.replace('(','').str.replace(')','')

# replace comlumn contain -
df['Tên Phân Loại']=convert_chuoi(df['Tên Phân Loại'])

# transform "column_name" from % to float
df['Tỷ lệ thoát Trang sản phẩm'] = convert_per(df['Tỷ lệ thoát Trang sản phẩm'])
df['Tỷ lệ chuyển đổi (theo lượt thêm vào giỏ hàng)'] = convert_per(df['Tỷ lệ chuyển đổi (theo lượt thêm vào giỏ hàng)'])
df['Tỷ lệ chuyển đổi (Đơn đã đặt)'] = convert_per(df['Tỷ lệ chuyển đổi (Đơn đã đặt)'])
df['Tỷ lệ chuyển đổi (Đơn đã xác nhận)'] = convert_per(df['Tỷ lệ chuyển đổi (Đơn đã xác nhận)'])
df['Tỷ lệ chuyển đổi (Từ Đơn đã đặt thanh Đơn đã xác nhận)'] = convert_per(df['Tỷ lệ chuyển đổi (Từ Đơn đã đặt thanh Đơn đã xác nhận)'])

# transform 'doanh số'
df['Doanh số (Đơn đã đặt) (VND)']=convert_int(df['Doanh số (Đơn đã đặt) (VND)'])
df['Doanh số (Đơn đã xác nhận) (VND)']=convert_int(df['Doanh số (Đơn đã xác nhận) (VND)'])

## replace blank = 0
df.fillna(0, inplace=True)

df.to_excel('D:\Python\convert\parentskudetail_123.xlsx', index=False)

### Cleaning data table 'CHAT1212'

df=pd.read_excel('D:\Python\convert\Chat_1212 .xlsx')
df.columns = df.columns.str.replace(' ', '_').str.replace('(','').str.replace(')','')
df['Lượt truy cập']=convert_int(df['Lượt truy cập'].astype('str'))
df['Doanh số(₫)']=convert_int(df['Doanh số(₫)'])
df['Tỷ lệ truy cập có chat']=convert_per(df['Tỷ lệ truy cập có chat'])
df['Tỷ lệ chuyển đổi (Yêu cầu phản hồi)']=convert_per(df['Tỷ lệ chuyển đổi (Yêu cầu phản hồi)'])
df['Tỷ lệ phản hồi Chat']=convert_per(df['Tỷ lệ phản hồi Chat'])
df['Tỷ lệ chuyển đổi (Phản hồi - Đơn được đặt)']=convert_per(df['Tỷ lệ chuyển đổi (Phản hồi - Đơn được đặt)'])
df['thời_gian_phản_hồi']=convert_chuoi(df['thời_gian_phản_hồi'])

#chuyển đổi thời gian thành giây
df['thời_gian_phản_hồi'] = pd.to_timedelta(df['thời_gian_phản_hồi'])
df['thời_gian_phản_hồi'] = df['thời_gian_phản_hồi'].dt.total_seconds()
df['thời_gian_phản_hồi']=df['thời_gian_phản_hồi'].astype('int')
print(type(df['thời_gian_phản_hồi']))

df.to_excel('D:\Python\convert\Chat_1212 .xlsx', index=False)

## Cleaning data table DISCOUNT

df=pd.read_excel('D:\Python\convert\discount_promotion_overview_123.xlsx')
df.columns = df.columns.str.replace(' ', '_').str.replace('(','').str.replace(')','')
# df['Doanh số (VND)']=convert_int(df['Doanh số (VND)'].astype('str'))
df['Doanh số trên mỗi Người mua (VND)']=df['Doanh số trên mỗi Người mua (VND)'].str.replace('.','').str.replace(',','')
df['Doanh_số_trên_mỗi_Người_mua_VND']=df['Doanh_số_trên_mỗi_Người_mua_VND']/100
# lưu lại file excel
df.to_excel('D:\Python\convert\discount_promotion_overview_123.xlsx', index=False)

## Cleaning data table PRODUCT

df = pd.read_excel('D:\Python\convert\productoverview_123.xlsx')
df.columns = df.columns.str.replace(' ', '_').str.replace('(','').str.replace(')','')
df['Tỷ lệ thoát Trang sản phẩm'] = convert_per(df['Tỷ lệ thoát Trang sản phẩm'])
df['Tỷ lệ chuyển đổi (theo lượt thêm vào giỏ hàng)'] = convert_per(df['Tỷ lệ chuyển đổi (theo lượt thêm vào giỏ hàng)'])
df['Tỷ lệ chuyển đổi (Đơn đã đặt)'] = convert_per(df['Tỷ lệ chuyển đổi (Đơn đã đặt)'])
df['Tỷ lệ chuyển đổi (Từ Đơn đã đặt thành Đơn đã xác nhận)'] = convert_per(
    df['Tỷ lệ chuyển đổi (Từ Đơn đã đặt thành Đơn đã xác nhận)'])
df['Tỷ lệ chuyển đổi (Đơn đã xác nhận)'] = convert_per(df['Tỷ lệ chuyển đổi (Đơn đã xác nhận)'])
df['Doanh số (Đơn đã đặt) (VND)'] = convert_int(df['Doanh số (Đơn đã đặt) (VND)'].astype('str'))
df['Doanh số (Đơn đã xác nhận) (VND)'] = convert_int(df['Doanh số (Đơn đã xác nhận) (VND)'].astype('str'))
df['Tỷ_lệ_thoát_Trang_sản_phẩm']/=100
df['Tỷ_lệ_chuyển_đổi_theo_lượt_thêm_vào_giỏ_hàng']/=100
df['Tỷ_lệ_chuyển_đổi_Đơn_đã_đặt']/=100
df['Tỷ_lệ_chuyển_đổi_Đơn_đã_xác_nhận']/=100
df['Tỷ_lệ_chuyển_đổi_Từ_Đơn_đã_đặt_thành_Đơn_đã_xác_nhận']/=100

df.to_excel('D:\Python\convert\productoverview_123.xlsx', index=False)

### Cleaning data table SALES

df=pd.read_excel('D:\Python\convert\sales_overview_123.xlsx')
df.columns = df.columns.str.replace(' ', '_').str.replace('(','').str.replace(')','')
df['Doanh số (Đơn đã đặt) (VND)']=convert_int(df['Doanh số (Đơn đã đặt) (VND)'].astype('str'))
df['Doanh số (Đơn đã xác nhận) (VND)']=convert_int(df['Doanh số (Đơn đã xác nhận) (VND)'].astype('str'))
df['Tỷ lệ chuyển đổi (Từ Lượt truy cập thành Đơn được đặt)']=convert_per(df['Tỷ lệ chuyển đổi (Từ Lượt truy cập thành Đơn được đặt)'])
df['Tỷ lệ chuyển đổi']=convert_per(df['Tỷ lệ chuyển đổi'])
df['Tỷ lệ chuyển đổi (Từ Đơn đã đặt thành Đơn đã xác nhận)']=convert_per(df['Tỷ lệ chuyển đổi (Từ Đơn đã đặt thành Đơn đã xác nhận)'])
df['Doanh_số_trên_mỗi_Người_mua_Đơn_đã_xác_nhận_VND']=df['Doanh_số_trên_mỗi_Người_mua_Đơn_đã_xác_nhận_VND'].str.replace('.','').str.replace(',','')
df['Doanh_số_trên_mỗi_Người_mua_Đơn_đã_xác_nhận_VND']=df['Doanh_số_trên_mỗi_Người_mua_Đơn_đã_xác_nhận_VND']/100
df['Tỷ_lệ_chuyển_đổi_Từ_Lượt_truy_cập_thành_Đơn_được_đặt']=df['Tỷ_lệ_chuyển_đổi_Từ_Lượt_truy_cập_thành_Đơn_được_đặt']/100
df['Tỷ_lệ_chuyển_đổi']=df['Tỷ_lệ_chuyển_đổi']/100
df['Tỷ_lệ_chuyển_đổi_Từ_Đơn_đã_đặt_thành_Đơn_đã_xác_nhận']=df['Tỷ_lệ_chuyển_đổi_Từ_Đơn_đã_đặt_thành_Đơn_đã_xác_nhận']/100
df.to_excel('D:\Python\convert\sales_overview_123.xlsx',index=False)

### Cleaning data table TRAFFIC

df=pd.read_excel('D:\Python\convert\Traffic_overview_123.xlsx',sheet_name='Tất cả')
df.columns = df.columns.str.replace(' ', '_').str.replace('(','').str.replace(')','')
df['Lượt_xem']=convert_int(df['Lượt_xem'].astype('str'))
df['Lượt_truy_cập']=convert_int(df['Lượt_truy_cập'].astype('str'))
df['Số_khách_truy_cập_mới']=convert_int(df['Số_khách_truy_cập_mới'].astype('str'))
df['Số_khách_truy_cập_hiện_tại']=convert_int(df['Số_khách_truy_cập_hiện_tại'].astype('str'))
df['Số_lượt_xem_trung_bình']=df['Số_lượt_xem_trung_bình'].str.replace(',','').astype('float')/100
df['Tỉ_lệ_thoát_trang']=convert_per(df['Tỉ_lệ_thoát_trang'])/100
# df['Thời_gian_xem_trung_bình'] = pd.to_timedelta(df['Thời_gian_xem_trung_bình'])
# df['Thời_gian_xem_trung_bình'] = df['Thời_gian_xem_trung_bình'].dt.total_seconds()

df.to_excel('D:\Python\convert\Traffic_overview_tatca.xlsx',index=False,sheet_name='Tất cả')

## Cleaning data table computer

df=pd.read_excel('D:\Python\convert\Traffic_overview_123.xlsx',sheet_name='Máy tính')
df.columns = df.columns.str.replace(' ', '_').str.replace('(','').str.replace(')','')
df['Lượt_xem']=convert_int(df['Lượt_xem'].astype('str'))
df['Lượt_truy_cập']=convert_int(df['Lượt_truy_cập'].astype('str'))
df['Số_khách_truy_cập_mới']=convert_int(df['Số_khách_truy_cập_mới'].astype('str'))
df['Số_khách_truy_cập_hiện_tại']=convert_int(df['Số_khách_truy_cập_hiện_tại'].astype('str'))
df['Số_lượt_xem_trung_bình']=df['Số_lượt_xem_trung_bình'].str.replace(',','').astype('float')/100
df['Tỉ_lệ_thoát_trang']=convert_per(df['Tỉ_lệ_thoát_trang'])/100

#
df.to_excel('D:\Python\convert\Traffic_overview_computer.xlsx',sheet_name='Máy tính',index=False)

### Cleaning data table mobile

df=pd.read_excel('D:\Python\convert\Traffic_overview_123.xlsx',sheet_name='Ứng dụng')
df.columns = df.columns.str.replace(' ', '_').str.replace('(','').str.replace(')','')
df['Lượt_xem']=convert_int(df['Lượt_xem'].astype('str'))
df['Lượt_truy_cập']=convert_int(df['Lượt_truy_cập'].astype('str'))
df['Số_khách_truy_cập_mới']=convert_int(df['Số_khách_truy_cập_mới'].astype('str'))
df['Số_khách_truy_cập_hiện_tại']=convert_int(df['Số_khách_truy_cập_hiện_tại'].astype('str'))
df['Số_lượt_xem_trung_bình']=df['Số_lượt_xem_trung_bình'].str.replace(',','').astype('float')/100
df['Tỉ_lệ_thoát_trang']=convert_per(df['Tỉ_lệ_thoát_trang'])/100

#
df.to_excel('D:\Python\convert\Traffic_overview_mobile.xlsx',sheet_name='Ứng dụng',index=False)