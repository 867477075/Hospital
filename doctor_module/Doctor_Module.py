from flask import Flask,Blueprint,render_template,request,Response
from dal.dbconnhelper import get_db_connection
from dal.dml import insert_data,authenticate,get_data
import json

doctor_object = Blueprint("doctor_object",__name__,url_prefix="/doctor_module")


@doctor_object.route('/login')
def doctor_login():

    return render_template("Doctor_login.html")

@doctor_object.route('/registration_form')
def register_doctor():

    return render_template("doctor_registration.html")

@doctor_object.route("/insert_data",methods=["POST"])
def push_data_into_db():
    request_data = request.form
    breakpoint()
    data_column = [x for x in request_data]
    data_value = [y for y in request_data.values()]
    result = insert_data("doctor_table", data_column, data_value)
    if result == 1:
        response_obj = {
            "massage": "Registration done  successfully"
        }
        return Response(json.dumps(response_obj))
    else:
        response_obj = {
            "massage": "There was problem in registration"
        }
        return Response(json.dumps(response_obj))


@doctor_object.route("/doctor_login", methods=["POST"]) # url binding
def doctor_login_done():
    request_data = request.form

    result = authenticate("doctor_table",request_data.get("username"), request_data.get("password"))

    user_name = request_data.get("username")
    if result == 1:
        data = get_data(user_name)
        breakpoint()
        return render_template("doctor_profile.html",data=data,username=user_name)
    else:
        response_obj = {
            "message": "Login Not Successfully"}
        return Response(json.dumps(response_obj))
