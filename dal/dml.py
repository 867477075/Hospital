from dal.dbconnhelper import get_db_connection


def authenticate(username_, password):
    conn = get_db_connection()

    cursor = conn.cursor()
    result = cursor.execute(f"""select * from hospital.admin_data where email_id='{username_}' and password_='{password}'""")

    return result


def insert_data(data_keys,data_values):
    data_value ="','".join(data_values)
    data_keys = ",".join(data_keys)
    conn = get_db_connection()
    cursor = conn.cursor()
    SQL = f"INSERT INTO hospital.admin_data({data_keys}) values('{data_value}');"

    result = cursor.execute(SQL)
    conn.commit()
    return result



