from config.default import db
from functools import partial

Column = db.Column
RequiredColumn = partial(Column, nullable=False)


class dbmodel(db.Model):
    __abstract__ = True
    __commentable__ = {'owner_class': None, 'owner_id': None, 'subject_id': None}
    id = Column('id', db.INT, primary_key=True, autoincrement=True)

    def json(self):
        raise NotImplementedError("Subclasses should implement this!")


class Asset(dbmodel):
    label       = RequiredColumn('label', db.VARCHAR(255), index=True)
    bought_date = RequiredColumn('bought_date', db.DATE)
    sold_date   = Column('sold_date', db.DATE)
    value       = RequiredColumn('value', db.INT, default=0)
    incomes     = db.relationship("Stream", backref=db.backref('asset', lazy='joined'), cascade="all, delete-orphan",
                                  lazy='dynamic')
    expenses    = db.relationship("Stream", backref=db.backref('asset', lazy='joined'), cascade="all, delete-orphan",
                                  lazy='dynamic')
    loans       = db.relationship("Loan", backref=db.backref('asset', lazy='joined'), cascade="all, delete-orphan",
                                  lazy='dynamic')

    @property
    def cashflow(self):
        return 3

    def json(self):
        return {}


class Stream(dbmodel):
    OCCURENCE = {'D': 'Daily', 'W': 'Weekly', 'M': 'Monthly', 'Q': 'Quarterly', 'Y': 'Yearly', 'N': 'NEVER'}
    label   = RequiredColumn('label', db.VARCHAR(255), index=True)
    start   = RequiredColumn('start', db.DATE)
    occurs  = RequiredColumn('occurs', db.VARCHAR(1))
    value   = RequiredColumn('value', db.FLOAT)

    def json(self):
        return {}


class Loan(dbmodel):
    label    = RequiredColumn('label', db.VARCHAR(255), index=True)
    start    = RequiredColumn('start', db.DATE)
    total    = RequiredColumn('total', db.FLOAT)
    apr      = RequiredColumn('apr', db.FLOAT)
    duration = RequiredColumn('duration', db.INT)

    @property
    def service_cost(self):
        return 3

    def json(self):
        result = super(Loan).json()
        return result


