import json
from dal.dml import authenticate,insert_data,get_data
from flask import Flask ,render_template,request,Response
from Appointment.appointment_module import blue_print
from doctor_module.Doctor_Module import doctor_object

app = Flask(__name__) # Flask Entry point

app.register_blueprint(blue_print)
app.register_blueprint(doctor_object)

@app.route('/ganesh')
def shree_ganesh():

    return "|| Shree Ganesh ||"


@app.route('/') # usl binding
def my_home():

    return render_template("Home.html")

@app.route('/Admin') # url binding
def my_admin():

    return render_template("Admin.html")


@app.route('/login',methods=["POST"]) # url binding
def login_done():
    request_data = request.form

    result = authenticate(request_data.get("username"), request_data.get("password"))

    if result == 1:
        result = get_data()
        return render_template("AdminProfile.html",data=result)
    else:
        response_obj = {
            "message": "Login Not Successfully"}
        return Response(json.dumps(response_obj))


@app.route('/registration')
def admin_registration():

    return render_template("Admin_registration.html")


@app.route('/insert_data', methods=["POST"])
def post_data():
    request_data = request.form # will get data in which format
    data_keys = [key_ for key_ in request_data if key_ != "confirm_pass"]
    data_values = [values_ for key_, values_ in request_data.items() if key_ != "confirm_pass"]

    result = insert_data(data_keys,data_values)
    response_obj = {
        "massage": "Record added successfully Now you can try to login into admin page"
    }
    return Response(json.dumps(response_obj))


if __name__ == "__main__":
    app.run(debug=True ,port=8080)
