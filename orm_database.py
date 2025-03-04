#######################################
# ORM数据库
#######################################

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from orm_model_userinfo import Base


# 异步引擎配置
engine = create_async_engine(
    "sqlite+aiosqlite:///userinfo.db",
    echo=True,   # 调试模式输出 SQL 语句
    future=True   # 启用 SQLAlchemy 2.0 特性
)

# 异步会话工厂
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)