# Giving a list of urls, print out the top 3 frequent filenames

urls = ["http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png"]


dic = {}

for i in urls:
    name  = i.split('/')[-1]
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1


for i in range(3):
    max_num = max(dic,key=dic.get)
    print max_num,dic[max_num]
    del dic[max_num]


