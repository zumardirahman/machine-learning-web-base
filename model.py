import pandas as pd
# from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import r2_score

# Membuat dataset manual prediksi harga handphone
data_hp = {
    'Merk':       [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],  # Samsung=1, iPhone=2, Xiaomi=3, Oppo=4, Realme=5
    'RAM_GB':     [4, 6, 8, 4, 8, 6, 12, 8, 4, 6, 12, 8, 6, 12, 4, 6, 8, 6, 12, 4, 6, 4, 8, 8, 12],
    'Storage_GB': [64, 128, 256, 64, 128, 256, 64, 128, 256, 128, 256, 128, 64, 256, 128, 64, 128, 256, 64, 128, 64, 128, 256, 128, 256],
    'Kamera_MP':  [12, 16, 24, 12, 48, 12, 48, 16, 12, 24, 12, 48, 16, 12, 24, 12, 48, 16, 12, 48, 16, 12, 48, 12, 24],
    'Baterai_mAh':[3000, 3500, 4000, 3000, 4500, 3500, 5000, 4000, 3000, 4500, 5000, 4000, 3500, 5000, 3000, 4000, 4500, 5000, 3000, 4000, 3500, 3000, 4500, 4000, 5000],
    'Harga':      [5000, 10000, 15000, 6000, 16000, 11000, 20000, 15000, 7000, 13000, 18000, 14000, 8000, 21000, 9000, 12000, 17000, 19000, 11000, 14000, 10000, 9000, 16000, 13000, 20000]
}

# Mengubah data ke DataFrame
df_hp = pd.DataFrame(data_hp)

# Konfigurasi Dataframe
# pd.set_option('display.float_format', '{:,.0f}'.format)  

# Membagi data menjadi fitur (X) dan target (y)
X = df_hp[['Merk', 'RAM_GB', 'Storage_GB', 'Kamera_MP', 'Baterai_mAh']]
Y = df_hp['Harga']

# Melatih model regresi linier
model_proses = LinearRegression()
model_proses.fit(X, Y)