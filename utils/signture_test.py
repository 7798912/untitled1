"""数据加密方法"""

import hashlib


# md5加密
def md5_string(str):
    md5 = hashlib.md5()  # 创建一个hashlib.md5()对象
    md5.update(str.encode("utf8"))  # 将参数转换为UTF8编码
    result = md5.hexdigest()
    return result   # 用十六进制输出加密后的数据


if __name__ == '__main__':
    str_in = '123456'  # 加密参数
    print(md5_string(str_in))
