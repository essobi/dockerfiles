FROM ubuntu:15.04  
  
MAINTAINER Sławek Ehlert <slafs@op.pl>  
  
# no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# get up to date  
RUN apt-get update --fix-missing  
  
# global installs [applies to all envs!]  
RUN apt-get install -y build-essential git  
RUN apt-get install -y python python-dev python-setuptools  
RUN apt-get install -y python-pip python-virtualenv  
RUN apt-get install -y nginx supervisor  
run apt-get install -y libffi-dev  
RUN apt-get install -y libjpeg-dev  
  
RUN pip install -U pip setuptools  
  
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get install -y -q
libxslt1-dev libxml2-dev libpq-dev libldap2-dev libsasl2-dev libssl-dev  
  
RUN apt-get install redis-server -y  
  
# install nginx  
run apt-get install \  
nginx \  
\--force-yes -y  
  
# install supervisor via apt-get because pip cannot work  
RUN apt-get install -y supervisor  
RUN pip install supervisor-stdout  
  
RUN mkdir -p /conf /data /wheels  
  
ADD requirements.txt /conf/  
  
RUN pip install -r /conf/requirements.txt  
  
EXPOSE 80  
  
VOLUME ["/data"]  
  
ADD sentry_docker_conf.py /conf/  
ADD sentry_run /usr/local/bin/  
  
ADD scripts/create_team_or_project.py /conf/  
ADD scripts/check_db_isalive.py /conf/  
ADD conf/redis.conf /etc/redis/redis.conf  
  
ADD conf/nginx.conf /etc/nginx/  
  
## remove default nginx config  
RUN rm /etc/nginx/sites-enabled/default  
  
## symlink the config file so easier to modify  
ADD conf/django-app.conf /etc/nginx/sites-enabled/  
  
## symlink supervisor config file  
ADD conf/app.conf /etc/supervisor/conf.d/  
  
## default command when you startup  
ENTRYPOINT ["supervisord", "-n", "-c", "/etc/supervisor/conf.d/app.conf"]  
  
# some cleanup  
RUN apt-get clean  
  

