dic_city = {'张三风': ['北京', '成都'], '李茉绸': ['上海', '广州', '兰州'], '慕容福': ['太原', '西安', '济南', '上海']}
for k, v in dic_city.items():
    print('{}去过{}个城市'.format(k, len(v)))
lst = [k for k, v in dic_city.items() if '上海' in v]
print('去过上海的有{}人，他们是{}'.format(len(lst), '、'.join(lst)))
