import time
import json
import hashlib
from urllib import request
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


class SignIn:
    def __init__(self, appkey=None, clerkid=None, password=None, serialno=None, stationid=None, types=None,
                 version=None, times=None, v=None, key=None):
        self.appkey = appkey
        self.clerkid = clerkid
        self.password = password
        self.serialno = serialno
        self.types = types
        self.version = version
        self.times = times
        self.v = v
        self.key = key
        if appkey is None:
            self.appkey = ("app_key", "620ffddf00d34500a62614271c23362T")
        if clerkid is None:
            self.clerkid = "0"
        if password is None:
            self.password = "123123"
        if serialno is None:
            self.serialno = "LX803478"
        if stationid is None:
            self.stationid = "21010002"
        if types is None:
            self.types = "70"
        if version is None:
            self.version = "7.22.00"
        if times is None:
            self.times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # times = "2019-01-22 09:56:42"
        if v is None:
            self.v = ("v", "1.0")
        if key is None:
            self.key = ("&key", "62xyY2Q1ZDkzMzMyNDEyOWEwNmUwZmVhNjBhZTI5r62")

    def token_key(self):
        sh = "="
        shs = "&"
        url = "https://114.242.206.226:6480/station/login"
        param_json = "param_json="
        timestamp = "&timestamp"
        sign_method = ("&sign_method", "MD5")
        # 前半段字符串
        appkeys = sh.join(self.appkey)
        appparam = [appkeys, param_json]
        appsparam = shs.join(appparam)
        # param_json字符串
        paramjion = {"serialNo": self.serialno, "stationId": self.stationid, "clerkId": self.clerkid,
                     "type": self.types, "password": self.password, "version": self.version}
        paramd = json.dumps(paramjion).encode(encoding='utf-8')
        paramdse = paramd.decode().strip()
        paramds = paramdse.replace(' ', '')
        # 拼MD5字符串
        timea = [timestamp, self.times]
        timese = sh.join(timea)
        vs = sh.join(self.v)
        timeses = [timese, vs]
        timev = shs.join(timeses)
        key = sh.join(self.key)
        mdf = (appsparam + "%s" % paramds + "%s" % timev + "%s" % key)
        # 获取MD5
        m = hashlib.md5()
        m.update(mdf.encode('utf-8'))
        md5 = m.hexdigest()
        # 拼接MD5
        signs = ["&sign", md5]
        signse = sh.join(signs)
        # 拼接请求的data
        signod = sh.join(sign_method)
        data = (appsparam + "%s" % paramds + "%s" % timev + "%s" % signod + "%s" % signse)
        # 请求post
        req = request.Request(url=url, data=data.encode('utf-8'))
        res = request.urlopen(req)
        res = res.read()
        # 打印获取返回信息
        print(res.decode().strip())
        # 截取token
        rese = json.loads(res.decode('utf-8'))
        reses = rese['content']
        msg = rese['msg']
        ret = rese['ret']
        if ret == 1101:
            token = reses['token']
            return token
        else:
            print(msg)


if __name__ == '__main__':
    print(SignIn().token_key())
