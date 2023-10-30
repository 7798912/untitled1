from config.yamlaction_test import read_yaml
import requests,pytest,time,os


#  增加共同操作fixtrue固件,类之前/之后执行对应操作
# @pytest.fixture(scope='class', autouse=True, params=['oper@2022', 'operation'])
# def content_mysql(request):
#     print('链接数据库')
#     yield request.param
#     print('断开数据库')


class TestMobile:
    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", read_yaml(r'C:\Users\dell\PycharmProjects\untitled1\data\login.yaml'))
    def test_login(self, caseinfo):
        """正确用户名，密码登录"""
        # test_url = base_test_url+"/api/auth/login" 根据配置拼接测试地址
        url = caseinfo['url']
        data = caseinfo['data']
        headers = caseinfo['headers']
        res = requests.post(url, json=data, headers=headers)
        # 断言
        assert res.status_code == 200

    @pytest.mark.parametrize("caseinfo", read_yaml(r'C:\Users\dell\PycharmProjects\untitled1\data\login.yaml'))
    def test_login1(self, caseinfo):
        """异常场景：用户名正确，密码为空"""
        url = caseinfo['url']
        data1 = caseinfo['data']['username']
        headers = caseinfo['headers']
        res1 = requests.post(url, json=data1, headers=headers)
        assert res1.status_code == 200

    @pytest.mark.parametrize("caseinfo", read_yaml(r'C:\Users\dell\PycharmProjects\untitled1\data\login.yaml'))
    def test_login2(self,caseinfo):
        """异常场景：用户名为空，密码正确"""
        url = caseinfo['url']
        data2 = caseinfo['data']['password']
        headers = caseinfo['headers']
        res2 = requests.post(url, json=data2, headers=headers)
        assert res2.status_code == 200

    @pytest.mark.parametrize("caseinfo", read_yaml(r'C:\Users\dell\PycharmProjects\untitled1\data\login.yaml'))
    def test_login3(self, caseinfo):
        """异常场景：用户名，密码为空"""
        url = caseinfo['url']
        headers = caseinfo['headers']
        res3 = requests.post(url, json=None, headers=headers)
        assert res3.status_code == 200

    @pytest.mark.parametrize("caseinfo", read_yaml(r'C:\Users\dell\PycharmProjects\untitled1\data\login.yaml'))
    def test_login4(self, caseinfo):
        """异常场景：用户名错误，密码正确"""
        url = caseinfo['url']
        data4 = {"username": "operatin", "password": 'password4'}
        headers = caseinfo['headers']
        res4 = requests.post(url, json=data4, headers=headers)
        assert res4.status_code == 200

    @pytest.mark.parametrize("caseinfo", read_yaml(r'C:\Users\dell\PycharmProjects\untitled1\data\login.yaml'))
    def test_login5(self, caseinfo):
        """异常场景：用户名正确，密码错误"""
        url = caseinfo['url']
        data5 = {"username": "operatin1", "password": 'password'}
        headers = caseinfo['headers']
        res5 = requests.post(url, json=data5, headers=headers)
        assert res5.status_code == 200


if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system("allure generate ../report")