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

def load_jobs_from_db():
  with engine.connect() as conn:
    result_jobs = conn.execute(text("select * from jobs"))
    all_jobs = result_jobs.all()
    column_names = result_jobs.keys() 
    
    job_dict = []
    
    for row in all_jobs:
      job_dict.append(dict(zip(column_names, row)))
  
    return job_dict