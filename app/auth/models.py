from datetime import datetime

from app import db , bcrypt  # app/__init__.py

from flask_login import UserMixin

from app import login_manager

from app.auth.register_email import register_email


class EmpIdscheck(db.Model):
    _tablename__ = 'empidscheck'

    id = db.Column(db.Integer, primary_key=True)
    emps_id = db.Column(db.Integer, unique=True,nullable=False)

    #def __init__(self, emps_id):
        #self.emps_id = emps_id

    #def __repr__(self):
        #return 'EmpIdscheck {}'.format(self.emps_id)

    def emp_user(cls, emps_id):
        empidscheck = cls(emps_id=emps_id)
        db.session.add(empidscheck)
        db.session.commit()
        return empidscheck


class EmpDetails(UserMixin , db.Model):
    __tablename__='empdetails'

    id=db.Column(db.Integer,primary_key=True)
    emp_id = db.Column(db.Integer, unique=True)
    emp_name=db.Column(db.String(60))
    emp_email=db.Column(db.String(60),unique=True,index=True)
    emp_gender=db.Column(db.String(10))
    emp_login=db.Column(db.Time)
    emp_logout=db.Column(db.Time)
    user_password=db.Column(db.String(200))
    confirm_password=db.Column(db.String(200))
    emp_hno = db.Column(db.String(200))
    emp_address=db.Column(db.String(200))
    emp_pincode = db.Column(db.Integer)
    registration_date=db.Column(db.DateTime,default=datetime.now)

    # Relationship
    #emp_id = db.Column(db.Integer, db.ForeignKey('EmpIdscheck.emps_id'))

    def check_password(self , password):
        return bcrypt.check_password_hash(self.user_password, password)

    # class methods belong to a class but are not associated with any class instance

    @classmethod

    def create_user(cls,empid,name,email,gender,login,logout,password,confirm,hno,address,pincode):
        empdetails=cls(emp_id=empid,
                 emp_name=name,
                 emp_email=email,
                 emp_gender=gender,
                 emp_login=login,
                 emp_logout=logout,
                 user_password=bcrypt.generate_password_hash(password).decode('utf-8'),
                 confirm_password=confirm,
                 emp_hno=hno,
                 emp_address=address,
                 emp_pincode=pincode)
        db.session.add(empdetails)
        db.session.commit()
        empdetails1 = EmpDetails.query.filter_by(emp_email=email).first()
        register_email(empdetails1.emp_email, empdetails1.emp_name)
        return empdetails


@login_manager.user_loader  #stores the active user's ID in the session

def load_user(id):
    return EmpDetails.query.get(int(id))  # convert unicode into integer. If user is invalid