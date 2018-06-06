FROM python:2.7  
MAINTAINER Alejandro Rocha <rochaa@tacc.utexas.edu>  
  
RUN apt-get update && apt-get install -y nginx supervisor ruby ruby-dev && gem
install sass compass && pip install uwsgi  
  
EXPOSE 80 443  
CMD ["supervisord", "-n"]  
  
# gettext for i18n  
RUN apt-get update && apt-get install -y gettext  
  
# kramdown for parsing static site content  
#RUN gem install kramdown  
# copy requirements.txt, deps, and config separate from the rest of the
project  
COPY requirements-frozen.txt /setup/requirements-frozen.txt  
  
### REMOVE THIS AFTER INTEGRATION IS COMPLETE  
#COPY deps /setup/deps  
###  
COPY docker-conf /setup/docker-conf  
  
# install pip dependencies  
RUN pip install -r /setup/requirements-frozen.txt  
  
# install non-pip dependencies  
### REMOVE THIS AFTER INTEGRATION IS COMPLETE  
#RUN cd /setup/deps/pytas && python setup.py install  
###  
# configure nginx, uwsgi, supervisord  
RUN \  
echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& rm /etc/nginx/sites-enabled/default \  
&& ln -s /setup/docker-conf/nginx-app.conf /etc/nginx/sites-enabled/ \  
&& ln -s /setup/docker-conf/supervisor-app.conf /etc/supervisor/conf.d/  
  
# setup project code  
COPY . /project  
WORKDIR /project  
  
# logs  
RUN mkdir /var/log/django  
  
# database migrations, if necessary  
# maybe remove this in the future? - @mrhanlon  
#RUN python manage.py migrate  
# translation messages, if necessary  
RUN python manage.py compilemessages  
  
# setup static assets  
RUN mkdir -p /var/www/static && mkdir -p /var/www/chameleoncloud.org/static &&
python manage.py collectstatic --noinput  

