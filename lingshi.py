import time
import json
import hashlib
from urllib import parse,request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
sh = "="
sh1 = "&"
appkey = ("app_key", "620ffddf00d34500a62614271c23362T")
param_json = "&param_json="
appkey1 = sh.join(appkey)
clerkId = "0"
password = "123123"
serialNo = "LX803478"
stationId = "21010002"
types = "70"
version = "7.22.00"
timestamp = "&timestamp"
times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# times = "2019-01-22 09:56:42"
times1 = [timestamp, times]
times2 = sh.join(times1)
v = ("v", "1.0")
v1 = sh.join(v)
sign_method = ("&sign_method", "MD5")
sign_method1 = sh.join(sign_method)
signs = [times2, v1]
signs1 = sh1.join(signs)
key = ("&key", "62xyY2Q1ZDkzMzMyNDEyOWEwNmUwZmVhNjBhZTI5r62")
ky1 = sh.join(key)
paramjion = {"serialNo": serialNo, "stationId": stationId, "clerkId": clerkId, "type": types, "password": password,
             "version": version}
paramd = json.dumps(paramjion).encode(encoding='utf-8')
paramds = paramd.decode().strip()
paramd1 = paramds.replace(' ', '')
params = (appkey1 + param_json + "%s" % paramd1 + "%s" % signs1)

params1 = (params + "%s" % ky1)
m = hashlib.md5()
m.update(params1.encode('utf-8'))
sign1 = m.hexdigest()
sign = ["&sign", sign1]
sign2 = sh.join(sign)
param = (params + "%s" % sign_method1 + "%s" % sign2)
url = "https://114.242.206.226:6480/station/login"
req = request.Request(url=url, data=param.encode('utf-8'))
res = request.urlopen(req)
res = res.read()
print(res.decode().strip())
res1 = json.loads(res.decode('utf-8'))
res2 = res1['content']
print(res2)
res3 = res2['token']
print(res3)
