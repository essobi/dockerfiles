FROM ubuntu:14.04  
MAINTAINER sken <sken [at] sken.biz>  
  
# os initialize  
RUN cp /usr/share/zoneinfo/Japan /etc/localtime  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN apt-get -y update  
RUN apt-get -y upgrade  
  
# install nginx  
RUN apt-get -y install nginx  
  
# install and activate python virtualenv  
#RUN apt-get -y install python-pip  
RUN apt-get -y install python  
#RUN pip install virtualenv  
RUN mkdir -p /srv/www/moin  
#RUN virtualenv /srv/www/moin/pythonenv  
#RUN source /srv/www/moin/pythonenv/bin/activate  
# download and install moin moin  
WORKDIR /tmp  
ADD http://static.moinmo.in/files/moin-1.9.8.tar.gz /tmp/moin-1.9.8.tar.gz  
#COPY moin-1.9.8.tar.gz /tmp/moin-1.9.8.tar.gz  
RUN tar xfz moin-1.9.8.tar.gz  
WORKDIR /tmp/moin-1.9.8  
RUN python setup.py install  
  
# deactivate python virtualenv  
#RUN deactivate  
# copy wiki to /srv/www/moin  
RUN cp -r ./wiki /srv/www/moin/  
  
# copy configs to wiki root directory  
WORKDIR /srv/www/moin/wiki/  
#RUN cp config/wikiconfig.py ./  
#RUN cp server/moin.wsgi ./  
ADD wikiconfig.py /srv/www/moin/wiki/wikiconfig.py  
ADD moin.wsgi /srv/www/moin/wiki/moin.wsgi  
  
# fix permission  
RUN chown www-data:www-data -R /srv/www/moin  
RUN chmod o-rwx -R /srv/www/moin  
  
# deploy with uwsgi  
RUN apt-get -y install uwsgi uwsgi-plugin-python  
ADD uwsgi.xml /srv/www/moin/wiki/uwsgi.xml  
  
# default set for nginx  
ADD default /etc/nginx/sites-available/default  
  
VOLUME /srv/www/moin/wiki/data  
EXPOSE 80  
CMD service nginx start && uwsgi -x /srv/www/moin/wiki/uwsgi.xml  

