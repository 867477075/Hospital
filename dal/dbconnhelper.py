import pymysql


def get_db_connection():
    conn = pymysql.Connect(host="127.0.0.1",port=3306,user="root",password="8080",db="Hospital")

    return conn


if __name__ == "__main__":
    result = get_db_connection()
    print(result)

