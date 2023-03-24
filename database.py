from sqlalchemy import create_engine,text
import os


db_connection = os.environ['db_freecodecamp_tutortial_key_string']


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