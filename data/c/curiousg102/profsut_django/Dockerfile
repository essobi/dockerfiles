FROM ubuntu:14.04  
  
MAINTAINER Miles Hutson  
  
RUN apt-get update -y  
  
RUN apt-get install -y python-dev\  
python-setuptools\  
libpq-dev  
  
RUN easy_install pip  
  
ADD . /opt/site  
  
RUN cd /opt/site && pip install -r requirements.txt  
  
RUN mkdir /var/eb_log  
  
ENV PROJECT_DIR /opt/site/djangoProfs  
  
#The four following environment variables are dummies to make development
easier  
ENV DJANGO_SECRET_KEY 6^klb956%pm_2lhg$j%242&-cbq&c)abska6@hdg-yc+@t(7&@'  
  
ENV VIDEOS_ZENCODER_KEY ksadfasgdasff  
  
ENV DEBUG true  
  
ENV AWS_ENVIRONMENT false  
  
CMD cd /opt/site && python profsUT/manage.py collectstatic --noinput\  
&& python profsUT/manage.py migrate --noinput\  
&& python profsUT/manage.py createsu\  
&& gunicorn -c /opt/site/gunicorn_config.py profsUT.wsgi --access-logfile
/var/eb_log/gunicorn_log  
  
EXPOSE 8001

