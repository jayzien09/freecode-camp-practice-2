from sqlalchemy import create_engine,text
import os


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
    
"""def load_job_from_db(id):
  with engine.connect() as conn:
    result_job = conn.execute(
      text("select * from jobs where id = :val").bindparams(val=id))
    row = result_job.all()
    row_key = result_job.keys()

    if row is None:
      return None
    else:
      row_dict = dict(zip(row_key[0], row[0]))
      return row_dict"""

def load_job_from_db(id):
    with engine.connect() as conn:
        result_job = conn.execute(
            text("SELECT * FROM jobs WHERE id = :id").bindparams(id=id)
        )
        row = result_job.all()
        row_key = result_job.keys()

        if len(row) == 0:
            return None
        else:
            print(dict(zip(row_key, row)))
            return dict(zip(row_key, row))
          

