FROM python:3.6.2-stretch  
MAINTAINER Jose Colella <josecolella@yahoo.com>  
  
#ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get install -y nginx supervisor  
  
# Setup flask application  
RUN mkdir -p /deploy/app  
COPY app /deploy/app  
COPY requirements.txt /deploy/app/requirements.txt  
RUN pip3 install --upgrade pip  
RUN pip3 install -r /deploy/app/requirements.txt  
  
# Setup nginx  
RUN rm /etc/nginx/sites-enabled/default  
COPY docker/flask.conf /etc/nginx/sites-available/  
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-
enabled/flask.conf  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Setup systemd  
#COPY gunicorn.service /etc/systemd/system/gunicorn.service  
# supervisor setup  
RUN mkdir -p /var/log/supervisor  
COPY docker/supervisord.conf /etc/supervisor/conf.d/  
COPY docker/gunicorn.conf /etc/supervisor/conf.d/  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]

