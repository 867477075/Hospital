from dal.dbconnhelper import get_db_connection


def authenticate(table_name,username_, password):
    conn = get_db_connection()

    cursor = conn.cursor()
    result = cursor.execute(f"""select * from hospital.{table_name} where email_id='{username_}' and password_='{password}'""")

    return result


def insert_data(table_name,data_keys,data_values):
    data_value ="','".join(data_values)
    data_keys = ",".join(data_keys)
    conn = get_db_connection()
    cursor = conn.cursor()
    SQL = f"INSERT INTO hospital.{table_name}({data_keys}) values('{data_value}');"
    breakpoint()
    result = cursor.execute(SQL)
    conn.commit()
    return result

def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = """select a.first_name ,d.doctor_name from appointment a
 inner join doctor_table d on a.id=d.doctor_id;"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return result



