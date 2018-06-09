FROM python:2.7.9  
MAINTAINER Vadim Caen <vadimcaen@gmail.com>  
  
ENV PYTHONPATH /app  
  
RUN apt-get update && apt-get install -y \  
libmysqlclient-dev\  
python-mysqldb  
  
ADD requirements.txt .  
RUN pip install -r requirements.txt  
  
CMD python /app/lyontour/dbscripts/db_create.py  
  
EXPOSE 8000  
ENTRYPOINT python /app/server.py

