FROM python:2.7  
MAINTAINER Richard Horne <rchrdhorne1@gmail.com  
  
ADD . /flask_app_config  
  
WORKDIR /flask_app_config  
  
RUN pip install flask uwsgi  
  
RUN uwsgi --build-plugin https://github.com/unbit/uwsgi-consul  
  
ENTRYPOINT [ "uwsgi", "--ini", "uwsgi-consul.ini", "--ini", "uwsgi-
consul.ini:server1" ]  
  
CMD []  

