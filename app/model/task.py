from datetime import datetime
from app import db

class Task(db.Model):
    __tablename__="task"

    task_id=db.Column("idtask",db.Integer,primary_key=True)
    task_name=db.Column("taskname",db.String(100))
    task_process=db.Column("task_process",db.Integer)
    user_name=db.Column("user",db.String(40))
    task_commit=db.Column("task_commit",db.Text)


    def __repr__(self):
        return "Task Id is:%d,Task Name is:%s" %(self.task_id,self.task_name)

    def to_json(self):
        return {
            "task_id":self.task_id,
            "task_name":self.task_name,
            "task_process":self.task_process,
            "user_name":self.user_name,
            "task_commit":self.task_commit
        }