FROM debian:jessie  
  
RUN apt-get update && apt-get install -y git freetds-dev python-dev python-pip
python-psycopg2 && pip install pymssql && pip install psycopg2  
ADD run.sh /root/run.sh  
RUN chmod +x /root/run.sh  

