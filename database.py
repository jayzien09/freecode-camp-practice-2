from sqlalchemy import create_engine,text

db_connection = "mysql+pymysql://sity5u6oymhxpjs7360w:pscale_pw_yhPz4gS8cWglL6KjUgSYiYVPXWMDgSedi57EcJ7Qtzi@ap-southeast.connect.psdb.cloud/trial_jaymark?charset=utf8mb4"


engine = create_engine(
    db_connection,
    connect_args={
        "ssl": {
            "ssl_cert": "/etc/ssl/cert.pem"
        }
    }
)

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.all()
    first_result = result_all[0]
    column_names = result.keys() 
    first_result_dict = dict(zip(column_names, first_result))
    print(first_result_dict)