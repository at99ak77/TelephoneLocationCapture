# -*- coding:utf-8 -*-

# 导入:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class SQLOutputer():
    Base = declarative_base()

    # 定义User对象:
    class MobileLocation(Base):
        # 表的名字:
        __tablename__ = 'mobile_location'

        # 表的结构:
        id = Column(Integer, primary_key=True)
        code = Column(String(10))
        location = Column(String(20))
        operator = Column(String(20))

    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://nero:123456@localhost:3306/nero')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()

    def __init__(self):
        self.cnt = 0

    def collect_data(self, data):
        if data is None:
            return
        self.cnt += 1
        ml = self.session.query(self.MobileLocation).filter(self.MobileLocation.code == str(data['code'])).first()
        if ml is None:
            ml = self.MobileLocation(code=str(data['code']), location=data['loc'], operator=data['type'])
            self.session.add(ml)
        else:
            ml.code = str(data['code'])
            ml.location = data['loc']
            ml.operator = data['type']
        if self.cnt > 99:
            self.commit()
            self.cnt = 0

    def commit(self):
        self.session.commit()

    def close(self):
        # 提交即保存到数据库:
        self.session.commit()
        # 关闭session:
        self.session.close()
