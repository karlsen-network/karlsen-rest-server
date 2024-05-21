from sqlalchemy import Column, String, BigInteger, UniqueConstraint, Index

from dbsession import Base


class Balance(Base):
    __tablename__ = 'balances'
    id = Column(BigInteger, primary_key=True)
    address = Column(String)
    amount = Column(BigInteger)

    __table_args__ = (UniqueConstraint('address',
                                       name='balances_address_key'),)


Index("idx_address", Balance.address)
Index("idx_amount", Balance.amount)
