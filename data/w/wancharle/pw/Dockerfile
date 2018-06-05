FROM python:2.7-alpine  
  
RUN apk update && \  
apk add --virtual build-deps gcc python-dev musl-dev && \  
apk add postgresql-dev  
  
RUN pip install flask peewee pip psycopg2 pymysql  
WORKDIR /root  
EXPOSE 80:5000  
VOLUME /root  
ENV FLASK_APP app.py  
ENV FLASK_DEBUG 1  
CMD sh  

