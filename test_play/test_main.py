# import pytest,datetime
#
# # 运行中的日志显示ASCII颜色
# if __name__ == "__main__":
#     now = datetime.datetime()
#     pytest.main(["test_debug.py",   # 测试用例
#                  "-v",  # -v 显示详细信息, -q 不输出环境信息, -s 显示程序中的打印和日志
#                  "--html=../report/report0729.html",   # 生成测试报告
#                  "--self-contained-html",  # 把css样式合并到html里
#                  "--color=yes",  # pytest 写入输出颜色
#                  ])

import datetime

appointedTime="2023-03-30"
appointed_time=datetime.datetime.strptime(appointedTime,"%Y-%m-%d")

curr_datetime=datetime.datetime.now()
minus_date=curr_datetime-appointed_time
print(minus_date.days)