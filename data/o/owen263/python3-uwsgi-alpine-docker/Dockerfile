FROM alpine:3.6  
MAINTAINER silencej owen263@gmail.com  
  
RUN apk add --no-cache uwsgi-python3 py3-psycopg2  
  
COPY requirements.txt /home/  
RUN pip3 install -r /home/requirements.txt  
VOLUME ["/home"]  
  

