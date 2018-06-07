FROM tiangolo/uwsgi-nginx-flask:python2.7  
RUN apt-get update  
RUN apt-get install -y libxml2-dev libxml2 libffi-dev git  
  
# build-base jpeg-dev zlib-dev openssl-dev  
ENV PYTHONPATH /mojp  
  
COPY requirements.txt /tmp/  
RUN pip install -r /tmp/requirements.txt  
  
COPY ./app /app  
COPY . /mojp  
COPY ./conf/docs_docker_nginx_conf /etc/nginx/conf.d/docs.conf  
  
VOLUME /etc/bhs  
  
EXPOSE 8081  

