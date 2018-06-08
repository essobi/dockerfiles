FROM ubuntu:16.04  
MAINTAINER Ikram Ali <mrikram1989@gmail.com>  
  
# Enable production settings by default; for development, this can be set to  
# `false` in `docker run --env`  
ENV DJANGO_PRODUCTION=true  
  
# Set terminal to be noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
# Enable MySQL root user creation without interactive input  
RUN echo 'mysql-server mysql-server/root_password password toor' | debconf-
set-selections  
RUN echo 'mysql-server mysql-server/root_password_again password toor' |
debconf-set-selections  
  
# Install packages  
RUN apt-get update && apt-get install -y \  
git \  
libmysqlclient-dev \  
mysql-server \  
nginx \  
python-dev \  
python-mysqldb \  
python-setuptools \  
supervisor \  
libffi-dev \  
libssl-dev \  
libpython2.7-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN easy_install pip  
RUN pip install urllib3[security] requests[security] ndg-httpsclient pyasn1  
  
# Configure Django project  
ADD . /code  
RUN mkdir /logs  
RUN mkdir /logs/nginx  
RUN mkdir /logs/gunicorn  
WORKDIR /code  
RUN pip install -r requirements.txt  
RUN chmod ug+x /code/initialize.sh  
  
# Expose ports  
# 80 = Nginx 8000 = Gunicorn 3306 = MySQL  
EXPOSE 80 8000 3306  
# Configure Nginx  
RUN ln -s /code/nginx.conf /etc/nginx/sites-enabled/djangoapps.conf  
RUN rm /etc/nginx/sites-enabled/default  
  
# Run Supervisor (i.e., start MySQL and Nginx)  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord"]

