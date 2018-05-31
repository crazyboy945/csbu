from datetime import datetime
from app import db


class Contract(db.Model):
    __tablename__ = 'contract'

    id = db.Column("id", db.Integer, primary_key=True)
    contract_number = db.Column("contract_number", db.String(
        45), unique=True, index=True, nullable=False)

    contract_price = db.Column("contract_price", db.Float, default=0.00)
    contract_date = db.Column("contract_date", db.Date(), index=True)
    contract_status = db.Column("contract_status", db.String(45), index=True)
    department = db.Column("department", db.String(20))
    custom = db.Column("custom", db.String(20))
    project_name = db.Column("porjectname", db.String(150))
    bill_price = db.Column("bill_price", db.Float, default=0.00)
    bill_date = db.Column("bill_date", db.Date())
    repayment = db.Column("repayment", db.Float, default=0.00)
    repayment_date = db.Column("repayment_date", db.Date)
    total_bill = db.Column("total_bill", db.Float, default=0.00)
    total_payment = db.Column("total_payment", db.Float, default=0.00)

    nbill_date = db.Column("nbill_date", db.Date())
    npayment_date = db.Column("npayment_date", db.Date())
    nbill_price = db.Column("nbill_price", db.Float, default=0.00)
    nrepayment = db.Column("nrepayment", db.Float, default=0.00)
    bills=db.relationship("Bill")
    repayments=db.relationship("Repayment")
    
    def get_bill_count(self):
        price=0
        for bill in self.bills :
            price+=bill.bill_price
        return price    

    def get_repayment(self):
        price=0
        for repayment in self.repayments:
            price+=repayment.price

    def __init__(self):
        self.contract_number = ""
        self.contract_status = ""
        self.contract_price = 0.00
        self.contract_date=datetime.date(datetime.strptime("0100-1-1","%Y-%m-%d"))
        self.department = 0.00
        self.custom = ""
        self.project_name = ""
        self.bill_price = 0.00
        self.bill_date=datetime.date(datetime.strptime("0100-1-1","%Y-%m-%d"))
        self.repayment = 0.00
        self.repayment_date=datetime.date(datetime.strptime("0100-1-1","%Y-%m-%d"))
        self.total_bill = 0.00
        self.total_payment = 0.00
        self.nbill_date=datetime.date(datetime.strptime("0100-1-1","%Y-%m-%d"))
        self.nbill_price = 0.00
        self.repayment_date=datetime.date(datetime.strptime("0100-1-1","%Y-%m-%d"))
        self.nrepayment = 0.00

    def to_json(self):
        return {
            "id": self.id,
            "contract_number": self.contract_number,
            "contract_status": self.contract_status,
            "contract_price": '%.2f' %self.contract_price,
            "contract_date": str(self.contract_date),
            "department": self.department,
            "custom": self.custom,
            "project_name": self.project_name,
            "bill_price": '%.2f' %self.bill_price,
            "bill_date": str(self.bill_date),
            "repayment": '%.2f' %self.repayment,
            "repayment_date": str(self.repayment_date),
           # "total_bill": '%.2f' %(self.total_bill if  self.total_bill else 0),
            "total_bill":"%.2f" % self.get_bill_count(),
            "total_payment":'%.2f' %self.total_payment,
            "nbill_date": str(self.nbill_date),
            "nbill_price": '%.2f' %(self.nbill_price if  self.nbill_price else 0),
            "nrepayment_date": str(self.repayment_date),
            "npayment": '%.2f' %(self.nrepayment if self.nrepayment else  0)
        }

    def __repr__(self):
        return "Contract ID is :%d, Contract Number is :%s " % (self.id, self.contract_number)


class Bill(db.Model):
    __tablename__="bill"

    id=db.Column("idbill",db.Integer,primary_key=True)
    contract_id=db.Column("contract_id",db.Integer,db.ForeignKey('contract.id'))
    bill_date=db.Column("bill_date",db.Date)
    bill_price=db.Column("bill_price",db.DECIMAL(10,2))


class Repayment(db.Model):
    __tablename__="repayment"
    id=db.Column("repaymentid",db.Integer,primary_key=True)
    contract_id=db.Column("contractid",db.Integer,db.ForeignKey('contract.id'))
    repayment_date=db.Column("repayment_date",db.Date)
    repayment_price=db.Column("repayment_price",db.DECIMAL(10,2))