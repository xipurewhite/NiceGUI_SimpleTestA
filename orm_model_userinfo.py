#######################################
# 数据表映射模型
#######################################
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String

class Base(DeclarativeBase):
    pass

# ORM，用户信息数据表
class UserInfo(Base):
    __tablename__ = "UserInfo"
    username = Column(String(50), primary_key=True, unique=True)
    password = Column(String(100), nullable=False)
