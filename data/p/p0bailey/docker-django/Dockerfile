  
FROM ubuntu:14.04  
MAINTAINER Phillip Bailey <phillip@bailey.st>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y install nginx sed python-pip python-dev uwsgi-plugin-python
supervisor  
  
RUN mkdir -p /var/log/nginx/example  
RUN mkdir -p /var/log/uwsgi/example/  
  
RUN rm /etc/nginx/sites-enabled/default  
  
COPY example.conf /etc/nginx/sites-available/  
  
RUN ln -s /etc/nginx/sites-available/example.conf /etc/nginx/sites-
enabled/example.conf  
  
RUN mkdir -p /var/log/supervisor  
COPY supervisor.example.conf /etc/supervisor/conf.d/supervisor.example.conf  
  
copy example /var/www/example  
  
RUN pip install -r /var/www/example/requirements.txt  
  
CMD ["/usr/bin/supervisord"]  

