lst_weather = [["周一", "16℃", "26℃", "多云", "1级", "优"], ["周二", "17℃", "27℃", "晴", "2级", "优"],
               ["周三", "16℃", "28℃", "晴", "3级", "优"], ["周四", "16℃", "25℃", "阴", "2级", "良"],
               ["周五", "15℃", "24℃", "阴", "2级", "良"], ["周六", "15℃", "25℃", "阴", "2级", "良"],
               ["周日", "14℃", "23℃", "小雨", "3级", "良"]]
lst_y = [x[0] for x in lst_weather if x[5] == "优"]
i = len(lst_y)
print("空气质量为优的天数:{},它们分别是：{}".format(i, ",".join(lst_y)))
lst_f = [x[0] for x in lst_weather if (int(x[2][:-1]) <= 25 and int(x[4][:-1]) < 3)]
print("风力低于3级且最高气温不超过25℃天数:{},它们分别是:{}".format(len(lst_f), ",".join(lst_f)))
lst_p = [x[0] for x in lst_weather if (int(x[1][:-1]) + int(x[2][:-1])) / 2 < 20]
print("平均气温低于20℃的天数:{},它们分别是:{}".format(len(lst_p), ",".join(lst_p)))
