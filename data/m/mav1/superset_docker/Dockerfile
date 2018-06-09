FROM python:2.7  
  
RUN apt-get update  
  
RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
python-pip libsasl2-dev libldap2-dev  
  
RUN apt-get install -y unixodbc unixodbc-dev  
  
RUN pip install --upgrade setuptools pip  
  
RUN pip install superset==0.18.4  
  
RUN pip install mysqlclient pymssql pyhive pyodbc  
  
RUN fabmanager create-admin --app superset --username admin --password admin
--firstname Yaming --lastname Ma --email mayaming1983@gmail.com  
  
RUN superset db upgrade  
  
RUN superset load_examples  
  
RUN superset init  
  
EXPOSE 8088  
  
CMD ["superset", "runserver"]  
  

