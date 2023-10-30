from config.yamlaction_test import read_yaml
import requests,yaml
# 获取测试数据
ret = read_yaml(r'C:\Users\dell\PycharmProjects\untitled1\data\login.yaml')[0]
url = ret.get('url')
username = ret.get('username')
password = ret.get('password')
headers = ret.get('headers')


class TestLogin:
    # 固定写入yaml文件
    def test_login(self,):
        """正确用户名，密码登录"""
    data = {
        "username": "operation",
        "password": "oper@2022"
            }
    res = requests.post(url, json=data, headers=headers)
    # 获取token
    token = res.json()['result']['token']
    # token存入yaml文件
    yaml_path = r"C:\Users\dell\PycharmProjects\untitled1\data\token.yaml"
    token_value = {'token': token}
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(token_value, stream=f)

    # 读取yaml文件
    def read_yaml_all(self, read_path):
        with open(read_path, "r", encoding="utf-8") as fs:
            data = yaml.load(stream=fs, Loader=yaml.FullLoader)
            print(data)
            return data

            # 清空yaml
    def clear_yaml(self, clear_path):
        with open(clear_path, encoding="utf-8", mode="w") as a:
            a.truncate()
