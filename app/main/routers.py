from flask import render_template, request, jsonify, make_response,flash,redirect,url_for
from flask_login import login_required,current_user
from sqlalchemy import extract,func

from . import main
from .. import auth
from .. import db
from datetime import datetime
from .. model.contract import Contract,Bill,Repayment
from .. model.task import Task

from . forms import newContractForm,editContractForm,ContractForm



@main.route("/")
@login_required
def index():
    return redirect(url_for('main.contract_sum'))

# 修改合同信息
@main.route("/contract/<int:id>", methods=['GET', 'POST'])
@login_required
def get_contract(id):
    con = Contract.query.get(id)
    if request.method == 'POST':
        con.contract_price = float(request.form["contract_price"])
        con.contract_date = datetime.strptime(
            request.form["contract_date"], '%Y-%m-%d')
        con.contract_status = request.form["contract_status"]
        con.department = request.form["department"]
        con.custom = request.form["custom"]
        con.contract_number = request.form["contract_number"]
        con.project_name = request.form["project_name"]
        con.bill_price = float(request.form["bill_price"])
        con.bill_date = datetime.strptime(
            request.form["bill_date"], '%Y-%m-%d')
        con.repayment = float(request.form["repayment"])
        con.repayment_date = datetime.strptime(
            request.form["repayment_date"], '%Y-%m-%d')
        con.total_bill = float(request.form["total_bill"])
        con.total_payment = float(request.form["total_payment"])
        con.nbill_date = datetime.strptime(
            request.form["nbill_date"], '%Y-%m-%d')
        con.npayment_date = datetime.strptime(
            request.form["npayment_date"], '%Y-%m-%d')
        con.npayment_date = datetime.strptime(
            request.form["npayment_date"], '%Y-%m-%d')
        con.project_name = request.form["project_name"]
        db.session.add(con)
        db.session.commit()
        db.session.flush()
        return redirect(url_for('main.get_contract_list'))
    return render_template('conmodal.html',con=con)


# 新建合同
@main.route("/contract/new", methods=['GET', 'POST'])
@login_required
def new_contract():

    con = Contract()

    if request.method == 'POST':
        con.contract_price = float(request.form["contract_price"])
        con.contract_date = datetime.strptime(
            request.form["contract_date"], '%Y-%m-%d')
        con.contract_status = request.form["contract_status"]
        con.department = request.form["department"]
        con.custom = request.form["custom"]
        con.contract_number = request.form["contract_number"]
        con.project_name = request.form["project_name"]
        con.bill_price = float(request.form["bill_price"])
        con.bill_date = datetime.strptime(
            request.form["bill_date"], '%Y-%m-%d')
        con.repayment = float(request.form["repayment"])
        con.repayment_date = datetime.strptime(
            request.form["repayment_date"], '%Y-%m-%d')
        con.total_bill = float(request.form["total_bill"])
        con.total_payment = float(request.form["total_payment"])
        con.nbill_date = datetime.strptime(
            request.form["nbill_date"], '%Y-%m-%d')
        con.npayment_date = datetime.strptime(
            request.form["npayment_date"], '%Y-%m-%d')
        con.nbill_price = float(request.form["nbill_price"])
        con.npayment_date = datetime.strptime(
            request.form["npayment_date"], '%Y-%m-%d')
        con.nrepayment = float(request.form["nrepayment"])
        con.project_name = request.form["project_name"]
        db.session.add(con)
        db.session.commit()
        db.session.flush()
    return redirect(url_for('main.get_contract_list'))

# 删除合同信息
@main.route("/contract/del/<int:id>",methods=["POST","GET"])
@login_required
def delete_contract(id):
    con = Contract.query.get(id)
    #form=ContractForm()
    if request.method == 'POST':

        try: 
            db.session.delete(con)
            db.session.commit()
            return render_template("message.htm",form={"title":"操作成功！","message":"成功删除id为:%d合同！"%id})
        except:
            return render_template("message.htm",form={"title":"操作失败","message":"未删除id为:%d的合同"%d})

    return render_template("delcon.htm",form=con)



# 获取合同数据
@main.route("/contract/list/")
@login_required
def get_contract_data():
    limit = request.args.get("limit",1,type=int)
    offset = request.args.get("offset",0,type=int)
    dept=request.args.get("dept","ALL")
    year=request.args.get("year",0,type=int)
    month=request.args.get("month",0,type=int)
    q=db.session.query(Contract)

    if dept!="ALL":
        q=q.filter(Contract.department==dept)
    if year>0:
        q=q.filter(extract("year",Contract.contract_date)==year)
    if month>0:
        q=q.filter(extract("month",Contract.contract_date)==month)
    cnt=q.count()
    cons=q.order_by("id desc").limit(limit).offset(offset).all()
    dat = []
    for con in cons:
        dat.append(con.to_json())

    return make_response(jsonify(code=0.00, msg="", total=cnt, rows=dat))

# 合同列表
@main.route("/contract",methods=["GET","POST"])
@login_required
def get_contract_list():    
    return render_template('conlist.htm')


@main.route('/contract/add/',methods=['GET', 'POST'])
@login_required
def addCon():
    form =newContractForm()
    if form.validate_on_submit():
        con = Contract()
        con.contract_number=form.contract_number.data
        con.contract_date=form.contract_date.data
        con.department=form.department.data
        con.custom=form.custom.data
        con.project_name=form.project_name.data
        con.contract_price=form.contract_price.data
        try:   
            db.session.add(con)
            db.session.commit()
            flash('新增合同成功！')
            return render_template("message.htm",form={"title":"操作成功！","message":"新增合同成功！"})
        except:
            flash("新增合同失败！")
            return render_template("message.htm",form={"title":"操作失败！","message":"新增合同失败！"})
    return render_template("conadd.htm",form=form)


@main.route('/contract/new/',methods=['GET', 'POST'])
@login_required
def newCon():
    form =newContractForm()
    if form.validate_on_submit():
        con = Contract()
        con.contract_number=form.contract_number.data
        con.contract_date=form.contract_date.data
        con.department=form.department.data
        con.custom=form.custom.data
        con.project_name=form.project_name.data
        con.contract_price=form.contract_price.data
        try:  
            db.session.add(con)
            db.session.commit()
            flash('新增合同成功！')
            return render_template("message.htm",form={"title":"操作成功！","message":"新增合同成功！"})
        except:

             return render_template("message.htm",form={"title":"操作失败！","message":"新增合同失败！"})
    return render_template("addcon.htm", form=form)

# 修改合同基本信息
@main.route('/contract/edit/<int:id>',methods=['GET', 'POST'])
@login_required
def editCon(id):
    form =newContractForm()
    con=Contract.query.get_or_404(id)
    if form.validate_on_submit():
        con.contract_number=form.contract_number.data
        con.contract_date=form.contract_date.data
        con.department=form.department.data
        con.custom=form.custom.data
        con.project_name=form.project_name.data
        con.contract_price=form.contract_price.data
        try:  
            db.session.add(con)
            db.session.commit()
            flash('修改合同成功！')
            return render_template("message.htm",form={"title":"操作成功！","message":"修改合同成功！"})
        except:
            return render_template("message.htm",form={"title":"操作失败！","message":"修改合同失败！"})
    form.id.data=con.id
    form.contract_number.data=con.contract_number
    form.contract_date.data=con.contract_date
    form.department.data=con.department
    form.custom.data=con.custom
    form.contract_price.data=con.contract_price
    form.project_name.data=con.project_name
    return render_template("conadd.htm", form=form)

# 修改开票、回款信息
@main.route('/contract/price/<int:id>',methods=['GET', 'POST'])
@login_required
def editPrice(id):
    form =editContractForm()
    con=Contract.query.get_or_404(id)
    if form.validate_on_submit():
        con.bill_date =form.bill_date.data
        con.bill_price=form.bill_price.data
        con.repayment=form.repayment.data
        con.repayment_date=form.repayment_date.data
        con.total_bill=form.total_bill.data
        con.total_payment=form.total_payment.data
        con.total_bill=form.total_bill.data
        con.nbill_date=form.nbill_date.data
        con.nbill_price=form.nbill_price.data
        con.nrepayment=form.nrepayment.data
        #print(con.to_json())
        try:
            db.session.add(con)
            db.session.commit()
        #db.session.flush()
            return render_template("message.htm",form={"title":"操作成功！","message":"修改合同成功！"})
        except:
            return render_template("message.htm",form={"title":"操作失败！","message":"修改合同失败！"})
    
    form.id.data=con.id
    form.bill_date.data=con.bill_date
    form.bill_price.data=con.bill_price
    form.repayment.data=con.repayment
    form.repayment_date.data=con.repayment_date
    form.total_bill.data=con.total_bill
    form.total_payment.data=con.total_payment
    form.nbill_date.data=con.nbill_date
    form.nbill_price.data=con.nbill_price
    form.npayment_date.data=con.npayment_date
    form.nrepayment.data=con.nrepayment
    return render_template("editcon.htm", form=form)

@main.route("/task")
@login_required
def get_task():

    tasks=Task.query.filter_by(user_name=current_user.username)

    task_sum_all=tasks.count()

    task_sum_process=tasks.filter(Task.task_process<100).count()

    task=tasks.order_by("task_process asc").all()

    task_sum={
        "process":task_sum_process,
        "all":task_sum_all,
        "complete":task_sum_all-task_sum_process
    }
    #for t in task:
    #    print(t.to_json())
    return render_template("tasklist.htm",task=task,tasksum=task_sum)

@main.route("/task/1")
@login_required
def get_task1():

    task=db.session.query(Task)
    task=task.filter(Task.user_name==current_user.username)
    task=task.filter(Task.task_process<100)
    
    task=task.order_by("task_process asc").all()

    return render_template("tasklist.htm",task=task)

@main.route("/task/0")
@login_required
def get_task0():

    task=db.session.query(Task)
    task=task.filter(Task.user_name==current_user.username).filter(Task.task_process==100)
    task=task.order_by("task_process asc").all()

    return render_template("tasklist.htm",task=task)

@main.route("/contract/sum")
@login_required
def contract_sum():
    current_year=datetime.now().year
    current_month=datetime.now().month
    # 获取开票汇总金额
    bill=db.session.query(func.sum(Bill.bill_price))
    bill=bill.filter(extract("year",Bill.bill_date)==current_year)
    # 年度汇总
    bill_year_sum=bill.scalar()
    # 月度汇总
    bill_month_sum=bill.filter(extract("month",Bill.bill_date)==current_month).scalar()

    # 获取回款汇总金额
    repayment=db.session.query(func.sum(Repayment.repayment_price))
    repayment=repayment.filter(extract("year",Repayment.repayment_date)==current_year)
    
    # 年度汇总
    repayment_year_sum=repayment.scalar()
    # 当月汇总
    repayment_month_sum=repayment.filter(extract("month",Repayment.repayment_date)==current_month).scalar()
    

    contract=db.session.query(func.sum(Contract.contract_price))
    contract=contract.filter(extract("year",Contract.contract_date)==current_year)
    # 本年合同总额
    contract_year_sum=contract.scalar()
    # 本月合同总额
    contract_month_sum=contract.filter(extract("month",Contract.contract_date)==current_month).scalar()


    cons=db.session.query(Contract)
    cons=cons.filter(extract("year",Contract.bill_date)==current_year)
    cons=cons.filter(extract("month",Contract.bill_date)==current_month)
    cons=cons.all()
    cons_proc=[]
    for con in cons:
        bills=db.session.query(func.sum(Bill.bill_price))
        bills=bills.filter(Bill.contract_id==con.id)

        bill=bills.filter(extract("year",Bill.bill_date)==current_year).scalar()
        if bill and bill>0:
            pass
        else:
           # print(con.to_json())
            cons_proc.append(con.to_json())

    



    return render_template("consum.htm", repayment_month_sum=repayment_month_sum,repayment_year_sum=repayment_year_sum,bill_year_sum=bill_year_sum,bill_month_sum=bill_month_sum,contract_year_sum=contract_year_sum,contract_month_sum=contract_month_sum,cons=cons_proc)

