from app import create_app , db

from app.auth.models import EmpDetails , EmpIdscheck

from sqlalchemy import exc

from app.catalog.models import EmpIds

flask_app = create_app('prod')
with flask_app.app_context():
    db.create_all()
    try:
        if not EmpDetails.query.filter_by(emp_id=10786).first():
            EmpDetails.create_user(empid=10786,
                            name="saikrishna",
                                email="krishnakrrish8@gmail.com",
                                gender="Male",
                                login="1:00 PM",
                                logout="10:00 PM",
                                password='secret',
                                confirm='secret',
                                hno='1-7-208,Maruthi nagar',
                                address="Santosh nagar,Hyderabad",
                                pincode=500060)
    except exc.IntegrityError:
            flask_app.run()
