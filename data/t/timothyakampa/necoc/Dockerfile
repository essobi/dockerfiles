# DOCKER-VERSION 0.0.1  
FROM ubuntu:14.04  
MAINTAINER Timothy Akampa timothyakampa@gmail.com  
  
ENV NGINX_SERVER_NAME 127.0.0.1  
ENV API_TOKEN 123232  
ENV LOAD_DATA False  
ENV EMAIL_PASSWORD XXXX  
  
RUN apt-get -qq update  
RUN apt-get -qqy install wget build-essential  
  
# ---- Deploy mongo db server ----  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' | tee /etc/apt/sources.list.d/10gen.list  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN apt-get -qqy update  
RUN apt-get -qqy install mongodb-10gen  
RUN mkdir -p /data/db  
VOLUME /data/db  
  
# ---- Install Bower ----  
RUN apt-get -qq update  
RUN apt-get -qqy install nodejs  
RUN apt-get -qqy install nodejs-legacy  
RUN apt-get -qqy install npm  
RUN npm install -g bower  
  
# --- Install image processing ---  
RUN apt-get -qqy install imagemagick libjpeg8-dev libfreetype6
libfreetype6-dev zlib1g-dev libpng12-dev  
  
# --- Install python, pip and virtualenv ----  
RUN apt-get -qqy install python python-dev  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN pip install virtualenv  
  
# ---Add Django Core project ----  
ADD . /necoc  
RUN cd /necoc/dms/client/app && bower install --allow-root --quiet  
RUN pip install -r /necoc/requirements.txt  
  
# --- Add Ngnix and uWISG ---  
RUN apt-get -qqy update && apt-get -qqy install nginx uwsgi uwsgi-plugin-
python  
ADD deployment/configs/necoc.conf /etc/nginx/conf.d/necoc.conf  
RUN sed -i "s/# server_names_hash_bucket_size 64/server_names_hash_bucket_size
64/" /etc/nginx/nginx.conf  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
ADD deployment/configs/necoc-uwsgi.ini /etc/uwsgi/apps-enabled/necoc-uwsgi.ini  
  
#--- Install Supervisord to run all background processes ---  
RUN apt-get -qq update  
RUN apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
RUN mkdir -p /var/log/mongodb  
RUN mkdir -p /var/log/nginx  
RUN mkdir -p /var/log/uwsgi  
ADD deployment/configs/supervisor.conf /etc/supervisor/conf.d/supervisor.conf  
  
VOLUME ["/var/log/"]  
  
# --- Add a starter script ----  
ADD deployment/scripts /scripts  
RUN chmod +x /scripts/run.sh  
RUN chmod +x /necoc/deployment/scripts/load_fixtures.sh  
RUN chmod +x /necoc/deployment/scripts/start_uwsgi.sh  
  
# ---MONGO ----  
EXPOSE 27017  
# --- Nginx ---  
EXPOSE 80 443 7999  
CMD "/scripts/run.sh"

