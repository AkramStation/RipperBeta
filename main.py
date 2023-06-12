import colorama
from colorama import Fore, Style
import socket

# تفعيل الألوان في الواجهة
colorama.init()

# طباعة النص الملون
print(Fore.YELLOW + '''
,--------.,--.  ,--.                  ,--.                   
'--.  .--'`--',-'  '-. ,--,--.,--,--, `--',--.,--.,--,--,--. 
   |  |   ,--.'-.  .-'' ,-.  ||      \,--.|  ||  ||        | 
   |  |   |  |  |  |  \ '-'  ||  ||  ||  |'  ''  '|  |  |  | 
   `--'   `--'  `--'   `--`--'`--''--'`--' `----' `--`--`--' 
                                                             
''' + Style.RESET_ALL)

# عرض رسالة الترحيب والتعليمات
print("Welcome To Titanium Controller")
print("Pls Chose One Of Our Service")
print("1 - Your Current Ip")
print("2 - How Much Botnets On The Stock")
print("3 - Attack Sent")

# اختيار الخدمة من المستخدم
service_choice = input("Service : ")

# تنفيذ الخدمة المختارة
if service_choice == '1':
    # الحصول على عنوان IP الخاص بالمضيف الحالي
    def get_local_ip():
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        return ip_address

    # تشغيل الكود للحصول على العنوان IP الخاص بك
    ip_address = get_local_ip()
    print("Your Ip Adress", ip_address)
else:
    print("خدمة غير صالحة. يرجى اختيار خدمة صحيحة.")

# إعادة إعداد الألوان الافتراضية
colorama.deinit()
