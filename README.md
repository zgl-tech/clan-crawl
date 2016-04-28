# clan-crawl

## 部署步骤

- 安装python, pip

- 安装依赖

```
    pip install -r requirements.txt
```

- 填写配置文件

```
    cp etc/config.py.sample etc/config.py
    cp etc/setting.py.sample etc/setting.py
    cp etc/scrapy.cfg.sample scrapy.cfg
```

其中config.py需要根据需求填写好各个变量

- 运行项目


```
    scrapy crawl clan
```
