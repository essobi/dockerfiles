FROM robo2025/python:3.6-alpine  
ENV PYTHONUNBUFFERED 1  
ADD . /project/roboserver  
  
WORKDIR /project/roboserver  
  
RUN pip install -r requirements.txt \  
&& mkdir -p /project/roboserver/logs \  
&& mkdir -p /project/roboserver/media  
  
CMD ["uwsgi", "/project/roboserver/inventory_management/wsgi/uwsgi.ini"]  

