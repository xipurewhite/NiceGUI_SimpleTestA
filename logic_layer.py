#######################################
# 逻辑层
#######################################
# import aiosqlite
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from contextvars import ContextVar
from orm_database import async_session
from orm_model_userinfo import UserInfo

# 校验账号密码格式
def vaildate_info(username: str, password: str) -> dict:
    if not username.strip() or not password.strip():
        return {'status': 'error', 'info': '用户名和密码不能为空！'}
    # 长度校验
    if len(username) < 3 or len(password) < 3:
        return {'status': 'error', 'info': '用户名和密码需>=3位！'}
    return {'status': 'success', 'info': ''}
    

# 用户登录验证
async def validate_login(username: str, password: str) -> dict:
    # 校验账号密码格式
    infores = vaildate_info(username, password)
    if infores['status'] == 'error':
        return {'status': 'negative', 'info': infores['info']}
    # 登录
    async with async_session() as session:
        stmt = select(UserInfo).where(UserInfo.username == username)
        result = await session.scalar(stmt)

        if not result:
            return {'status': 'negative', 'info': '用户名不存在！'}
        elif result.password != password:
            print(f"UserName: {username}, Password: {password}, PasswordDB: {result.password}")
            return {'status': 'negative', 'info': '密码错误！'}
        else:
            return {'status': 'positive', 'info': f"登录成功: {username}, {result.password}！"}

# 用户注册验证
async def validate_register(username: str, password: str, confirm: str) -> dict:
    # 校验账号密码格式
    infores = vaildate_info(username, password)
    if infores['status'] == 'error':
        return {'status': 'negative', 'info': infores['info']}
    if password != confirm:
        return {'status': 'negative', 'info': '两次输入密码不一致！'}
    # 注册
    async with async_session() as session:
        # 检查用户是否存在
        result = await session.get(UserInfo, username)
        if result:
            return {"status": "negative", "info": "用户名已存在！"}
        try:
            # 创建新用户
            new_user = UserInfo(username=username, password=password)
            session.add(new_user)
            await session.commit()
            return {'status': 'positive', 'info': f"注册成功: {username}"}
        except IntegrityError:
            await session.rollback()
            return {'status': 'negative', 'info': '数据库异常！'}

# 获取当前登录用户
async def get_user(username: str) -> dict:
    async with async_session() as session:
        stmt = select(UserInfo).where(UserInfo.username == username)
        result = await session.scalar(stmt)
        if not result:
            return {'info': '用户名不存在！'}
        return {'username': result.username, 'password': result.password}