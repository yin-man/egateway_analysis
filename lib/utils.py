import json
import pytz
import copy
import time
import argparse
import datetime
import traceback
import random
import hashlib

class Utils(object):
    x = ""
    y = None

    @classmethod
    def curl(cls, url, args=None, headers={}, timeout=12, retry=3, method='GET'):
        """wrap http request

        Args:
                url: A string
                headers: A map
                args: post json param
                timeout: A integer

        Returns:
                ret: mixed
        
        """
        import requests
        index, retry_times = 0, retry
        msg = "request: %s, args: %s, headers: %s" % (url, args, headers)
        if isinstance(args, dict) or isinstance(args, list):
            args = json.dumps(args)
        while index < retry_times:
            try:
                ret = getattr(requests, method.lower())(url, params=args,
                        data=args, headers=headers, timeout=timeout)
                if ret.status_code >= 200 and ret.status_code < 300:
                    if method.lower() in ["head", "HEAD"]:
                        return ret.headers
                    return ret.text
                else:
                    raise Exception(ret.status_code)
            except Exception as e:
                index += 1
                if index >= retry_times:
                    raise Exception("%s %s %s" % (msg, str(e), ret.text))

    @classmethod
    def deepupdate(cls, target, src):
        if not isinstance(target, dict) or not isinstance(src, dict):
            return
        for k, v in src.items():
            if k not in target:
                target[k] = copy.deepcopy(v)
                continue
            if type(v) == dict:
                cls.deepupdate(target[k], v)
            else:
                target[k] = copy.copy(v)

    @classmethod
    def md5(cls, s):
        m1 = hashlib.md5()
        m1.update(s.encode('utf-8'))
        return m1.hexdigest()

    @classmethod
    def md5sum(cls, filename, block_size=65536):
        hash = hashlib.md5()
        with open(filename, "rb") as f:
            for block in iter(lambda: f.read(block_size), b""):
                hash.update(block)
        return hash.hexdigest()

    @classmethod
    def local_to_utc(cls, local_ts, utc_format='%Y-%m-%dT%H:%MZ'):

        local_tz = pytz.timezone('Asia/Chongqing')
        local_format = "%Y-%m-%d %H:%M"
        time_str = time.strftime(local_format, time.localtime(local_ts))
        dt = datetime.datetime.strptime(time_str, local_format)
        local_dt = local_tz.localize(dt, is_dst=None)
        utc_dt = local_dt.astimezone(pytz.utc)
        return utc_dt.strftime(utc_format)

    @classmethod
    def utc_to_local(cls, utc_time_str, utc_format='%Y-%m-%dT%H:%M:%SZ', local_format='%Y-%m-%d %H:%M:%S'):

        local_tz = pytz.timezone('Asia/Chongqing')
        utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)
        local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
        time_str = local_dt.strftime(local_format)
        return int(time.mktime(time.strptime(time_str, local_format)))

    @classmethod
    def ts_to_str(cls, ts, fmt='%m-%d %H:%M'):
        return time.strftime(fmt, time.localtime(ts))

    @classmethod
    def judge_bool(cls, bstr):
        lbstr = bstr.lower()
        if lbstr in ["true", "y", "1", "yes"]:
            return True
        elif lbstr in ["false", "n", "0", "no"]:
            return False
        else:
            raise argparse.ArgumentTypeError("Unsupported value encountered.")

    @classmethod
    def ts_to_chunk(cls, start_ts, end_ts, interval):

        ret = []
        ets, sub = start_ts, end_ts - start_ts
        count, left = int(sub / interval), sub % interval
        for i in range(0, count):
            sts = start_ts + i * interval
            ets = sts + interval
            ret.append([sts, ets])
        if left:
            ret.append([ets, end_ts])

        return ret

    @classmethod
    def get_chunked_data(cls, data, chunk_size=200):
        return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]


if __name__ == "__main__":
    #print(Utils.ts_to_chunk(1541005200, 1542646800, 86400))
    #print(Utils.judge_bool("yes"))
    #print(Utils.judge_bool("n"))
    #print(Utils.judge_bool("p"))
    #target = {
    #    "a": "b",
    #    "c" : {
    #        "d": "e" ,   
    #    },      
    #    "b": [2],
    #}
    #src = {
    #    "c": {
    #        "d": "f",
    #        "f": "g",
    #    },
    #    "b": "s",
    #}
    #Utils.deepupdate(target, src)
    #print(target)

    #ret = Utils.curl("http://10.0.0.0:9095/api/v1/alerts", args=[{'annotations': {'resource_url': '', 'status': '1', 'msg': '[ERR][\u81ea\u5efahttp\u76d1\u63a7][zj2-jh-tnm-tmc19.zj2][117.149.38.246][\u53ef\u7528\u6027\u4f4e]'}, 'labels': {'metric': 'http_probe', 'area': 'zhejiang', 'vip': '117.149.38.246', 'domain': 'www.isurecdn.com', 'isp': 'cmnet', 'alertname': 'http_probe'}, 'at': '2018-07-20T06:55:00Z'}], method='POST')
    #print(ret)
    t = {"con": {"tcp_retrans": {"default_setting": {}}}}
    s = {"con": {"tcp_retrans": {"special_setting": {}, "default_setting": "aaa"}}}
    Utils.deepupdate(t, s)
    print(t)