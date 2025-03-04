# 项目说明

+ 该项目实现了简单的登陆注册页面，并通过数据库保存用户信息，项目通过Docker部署运行。
+ 构成：
  + 基于NiceGUI实现的用户登录注册界面布局
  + 基于TailwindCSS的页面美化处理
  + 基于SQLAlchemy实现的基于ORM模型的异步数据库访问
  + 简单的API端点示范
+ 依赖管理：基于Poetry2的依赖管理
+ Docker运行环境

# 主要文件结构

+ ui_layer.py：登录注册界面的视图层
+ logic_layer.py：登录注册业务逻辑实现
+ ORM模型：用户数据信息
  + orm_model_userinfo.py：用户表映射
  + orm_database.py：数据库管理
+ Dockerfile：用于部署docker镜像
+ pyproject.toml：项目依赖信息（基于Poetry）
+ userinfo.db：数据库文件

# 项目运行步骤

## 测试环境

+ python 2.12.8
+ poetry 2.1.1

## 本地运行

**1.安装依赖**

```
poetry install --no-root
```

**2.运行测试**

```
poetry run python ui_layer.py
```

## 基于Docker部署

**1.创建docker镜像**

```
docker build -t my-python-test1 .
```

**2.执行docker镜像**

```
docker run -p 8080:8080 my-python-test1
```

**3.打开浏览器**

```
打开localhost:8080进入登录页面
```

**API测试**

```
名称：getuser?username=用户名
返回：用户名和用户密码
举例：localhost:8080/api/getuser?username=abc
```

# 开发思路

+ 根据需求区分功能部分
  + 界面部分
    + 界面构成组件
    + UI布局：次要考虑
    + CSS：次要考虑
  + 业务逻辑部分
    + 登录，注册功能
      + 1.检查用户信息的有效性
      + 2.访问数据库获取/写入信息
    + API调用
  + 数据库管理部分
    + 用户数据管理逻辑
    + 数据库控制逻辑

# 遇到的问题

**Docker构建镜像时资源下载失败**

```
1.配置适合的源
2.使用代理并配置环境变量
$env:HTTP_PROXY="http://127.0.0.1:9788"
$env:HTTPS_PROXY="http://127.0.0.1:9788"
```

**Docker构建镜像时pip无法找到需要的Poetry版本**

```
RUN pip install poetry==1.8.5
RUN poetry self update 2.1.1 # 升级版本
```







