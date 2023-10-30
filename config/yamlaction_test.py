import yaml,pytest


def read_yaml(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
        result = yaml.load(data, Loader=yaml.FullLoader)
        ret = list()
        for k in result.keys():
                v = result[k]
                v["key"] = k
                ret.append(v)
        return ret


if __name__ == '__main__':
#     result = read_yaml(r'C:\Users\dell\PycharmProjects\untitled1\data\login.yaml')
#     print(result)
    pytest.main()

