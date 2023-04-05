from flask import Flask ,render_template,request,Blueprint, Response
from dal.dbconnhelper import get_db_connection
from dal.dml import insert_data,authenticate,get_data
import json

import pymysql
blue_print = Blueprint("appointment",__name__,url_prefix="/appointment")


@blue_print.route('/')
def index():

    return render_template("index.html")

@blue_print.route("/appointment")
def register_for_appointment():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select concat(doctor_id,'_',doctor_name,'_',specialist) as Name_of_Doctor from doctor_table;")
    result = cursor.fetchall()
    result = ["".join(x) for x in result]
    return render_template("appointment_form.html",data=result)


@blue_print.route('/register_appointment',methods=["POST"])
def register():
    request_data = request.form
    data_column = [",".join(["id","Doctor_name","specialist"]) if x == "doctor_choice" else x for x in request_data ]
    data_value = ["','".join(y.split('_')) if x == "doctor_choice" else y for x , y in request_data.items()]
    result = insert_data("appointment",data_column,data_value,)
    if result == 1:
        response_obj = {
            "massage": "Your request for an appointment added successfully"
        }
        return Response(json.dumps(response_obj))
    else:
        response_obj = {
            "massage": "There was problem in request Please wait and try later"
        }
        return Response(json.dumps(response_obj))



if __name__ == "__main__":
    blue_print.run(debug=True)
