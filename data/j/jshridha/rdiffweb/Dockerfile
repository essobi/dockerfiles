FROM phusion/baseimage:0.9.17  
MAINTAINER jshridha <jshridha@gmail.com>  
  
# Install dependencies  
RUN apt-get update && apt-get install -q -y --no-install-recommends \  
python-cherrypy3 \  
python-pysqlite2 \  
libsqlite3-dev \  
python-jinja2 \  
python-setuptools \  
python-babel \  
rdiff-backup \  
supervisor  
  
RUN apt-get install wget  
  
# apt-get clean && \  
# rm -rf /var/lib/apt/lists/*  
# Download and install rdiffweb  
RUN wget --no-check-certificate -O rdiffweb.tar.gz
https://github.com/ikus060/rdiffweb/archive/master.tar.gz && \  
tar zxf rdiffweb.tar.gz && \  
cd rdiffweb-* && \  
python setup.py build && \  
sudo python setup.py install && \  
sudo update-rc.d rdiffweb defaults  
  
VOLUME /config /backups /restores  
  
EXPOSE 8080  
ADD *.conf /etc/supervisor/conf.d/  
  
ADD start.sh /root/start.sh  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]  

