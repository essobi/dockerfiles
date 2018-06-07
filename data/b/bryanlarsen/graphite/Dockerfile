  
FROM ubuntu:12.04  
# install dependencies
--------------------------------------------------------  
RUN echo 'deb http://archive.ubuntu.com/ubuntu precise main universe' >
/etc/apt/sources.list.d/universe.list  
RUN apt-get -y update  
  
RUN apt-get -y --force-yes install vim python-flup expect git memcached
sqlite3 libcairo2 libcairo2-dev python-cairo pkg-config wget python-dev
python-pip nginx-light  
  
RUN pip install txAMQP  
  
RUN pip install supervisor  
RUN mkdir /var/log/supervisor  
  
# # get source code
-------------------------------------------------------------  
RUN cd /usr/local/src && git clone https://github.com/graphite-
project/graphite-web.git  
  
RUN cd /usr/local/src && git clone https://github.com/graphite-
project/whisper.git  
  
RUN cd /usr/local/src && git clone https://github.com/graphite-
project/carbon.git  
  
# # install apps
----------------------------------------------------------------  
RUN cd /usr/local/src/graphite-web && pip install -r requirements.txt &&
python ./setup.py install  
  
RUN cd /usr/local/src/whisper && python ./setup.py install  
  
RUN cd /usr/local/src/carbon && pip install -r requirements.txt && python
./setup.py install  
  
add ./nginx.conf /etc/nginx/nginx.conf  
add ./supervisord.conf /usr/local/etc/supervisord.conf  
  
# Add graphite config  
add ./initial_data.json /opt/graphite/webapp/graphite/initial_data.json  
add ./local_settings.py /opt/graphite/webapp/graphite/local_settings.py  
add ./carbon.conf /opt/graphite/conf/carbon.conf  
add ./storage-schemas.conf /opt/graphite/conf/storage-schemas.conf  
add ./create_superuser.py /opt/graphite/webapp/graphite/create_superuser.py  
  
add ./run.sh /run.sh  
run chmod +x /run.sh  
  
# Nginx  
expose 80  
# Carbon line receiver port  
expose 2003  
# Carbon pickle receiver port  
expose 2004  
# Carbon cache query port  
expose 7002  
volume ["/opt/graphite/storage"]  
  
cmd ["/run.sh"]  
  

