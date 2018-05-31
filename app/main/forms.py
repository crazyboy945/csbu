from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, DecimalField, DateField, IntegerField,HiddenField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField


class newContractForm(FlaskForm):
    id = HiddenField('合同ID')  
    contract_number = StringField('合同编号', validators=[Length(0, 45,message="长度不能超过45个字符！")])
    contract_date = DateField('合同日期', validators=[DataRequired("合同日期必须为日期，例如：2018-1-1 ")])
    contract_price = DecimalField("合同金额", validators=[DataRequired("合同金额必须为数字！")])
    custom = StringField('客户', validators=[DataRequired("客户必填"), Length(0, 20)])
    project_name= StringField('项目名称', validators=[DataRequired("项目名称必填"), Length(0, 150)])
    department= SelectField('部门', validators=[DataRequired("部门必填"), Length(0, 20)])
    contract_status=StringField('合同状态',validators=[Length(0, 45)])
    submit = SubmitField('保存')

    def __init__(self, *args, **kwargs):
        super(newContractForm, self).__init__(*args, **kwargs)
        self.department.choices = [("SAP", "SAP"), ("ORACLE", "ORACLE"), ("SIEBEL", "SIEBEL"),("JR", "JR")]


class ContractForm(FlaskForm):
    id = HiddenField('合同ID')  
    contract_number = StringField('合同编号', validators=[Length(0, 45,message="长度不能超过45个字符！")])
    contract_date = DateField('合同日期', validators=[DataRequired("合同日期必须为日期，例如：2018-1-1 ")])
    contract_price = DecimalField("合同金额", validators=[DataRequired("合同金额必须为数字！")])
    custom = StringField('客户', validators=[DataRequired("客户必填"), Length(0, 20)])
    project_name= StringField('项目名称', validators=[DataRequired("项目名称必填"), Length(0, 150)])
    department= SelectField('部门', validators=[DataRequired("部门必填"), Length(0, 20)])
    contract_status=StringField('合同状态',validators=[Length(0, 45)])
    bill_price = DecimalField("开票金额")
    bill_date = DateField("开票日期")
    repayment = DecimalField("回款金额")
    repayment_date = DateField("回款日期")
    total_bill = DecimalField("累计开票")
    total_payment = DecimalField("累计回款")
    nbill_date = DateField("下次开票日期")
    nbill_price = DecimalField("下次开票金额")
    npayment_date = DateField("下次回款日期")
    nrepayment = DecimalField("下次回款金额")
    submit = SubmitField('保存')
    delete=SubmitField('删除')
    
    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)
        self.department.choices = [("SAP", "SAP"), ("ORACLE", "ORACLE"), ("SIEBEL", "SIEBEL"),("JR", "JR")]


class editContractForm(FlaskForm):
    id = HiddenField('合同ID')    
    bill_price = DecimalField("开票金额")
    bill_date = DateField("开票日期")
    repayment = DecimalField("回款金额")
    repayment_date = DateField("回款日期")
    total_bill = DecimalField("累计开票")
    total_payment = DecimalField("累计回款")
    nbill_date = DateField("下次开票日期")
    nbill_price = DecimalField("下次开票金额")
    npayment_date = DateField("下次回款日期")
    nrepayment = DecimalField("下次回款金额")
    submit = SubmitField('保存')

    
