FROM frolvlad/alpine-python3  
  
RUN apk add --update git  
  
WORKDIR /app/  
  
ADD requirements.txt /app/requirements.txt  
RUN pip3 install gunicorn \  
&& pip3 install -r /app/requirements.txt  
  
ADD api /app/api  
ADD migrations /app/migrations  
ADD manager.py /app/manager.py  
ADD server.py /app/server.py  
  
ADD docker_config.json /app/api/conf/  
  
RUN python3 manager.py db upgrade  
  
# exposed port  
EXPOSE 5000  
CMD gunicorn -w 4 -b 0.0.0.0:5000 api:application  

