#ehentai_picker

一个 ehentai 爬虫。纯属新人练手项目。

请在

```python
def mkdir(self , path):
        front_pass = "/Users/Anhedonia/Desktop/workspace/myproject/ehentai_picker/"
        isExists = os.path.exists(os.path.join(front_pass, path))

        if not isExists:
            os.makedirs(os.path.join(front_pass,path))
            os.chdir(front_pass+'/'+path)
        else:
            os.chdir(front_pass+'/'+path)
```

内，自行更改 `front_pass`的量，来更改下载地址。



### 接下来的打算：

- [ ] 增加GIF支持

- [ ] 打包环境
- [ ] 添加 GUI
- [ ] 打包成 EXE
- [ ] 找到更好的代理