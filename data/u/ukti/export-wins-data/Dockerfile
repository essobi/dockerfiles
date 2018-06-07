FROM python:3.6  
RUN apt-get update && apt-get install -y postgresql-client xmlsec1  
  
RUN mkdir /app  
  
COPY alice /app/alice  
COPY data /app/data  
COPY gunicorn /app/gunicorn  
COPY mi /app/mi  
COPY users /app/users  
COPY wins /app/wins  
COPY fixturedb /app/fixturedb  
COPY sso /app/sso  
COPY core /app/core  
COPY fdi /app/fdi  
COPY csvfiles /app/csvfiles  
  
COPY requirements.txt /app/requirements.txt  
COPY manage.py /app/manage.py  
COPY start.sh /app/start.sh  
COPY start-wait-for-db.sh /app/start-wait-for-db.sh  
  
WORKDIR /app  
RUN pip install -r /app/requirements.txt  
  
EXPOSE 8000  
CMD ./start.sh  

