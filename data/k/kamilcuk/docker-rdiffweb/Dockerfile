FROM alpine  
MAINTAINER Kamil Cukrowski <kamilcukrowski@gmail.com>  
  
# Install dependencies  
RUN apk --no-cache add tar \  
python \  
py-pysqlite \  
sqlite \  
py-jinja2 \  
py-setuptools \  
py-babel \  
py-psutil \  
py-future \  
py-pip \  
rdiff-backup \  
wget && \  
pip install cherrypy && \  
rm -rf /usr/share/locale/* && \  
rm -rf /usr/share/man/* && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Download and install rdiffweb  
RUN wget --no-check-certificate -O rdiffweb.tar.gz
https://github.com/ikus060/rdiffweb/archive/master.tar.gz && \  
tar zxf rdiffweb.tar.gz && \  
cd rdiffweb-* && \  
python setup.py install && \  
mkdir -p /etc/rdiffweb && \  
cp rdw.conf /etc/rdiffweb/ && \  
cd .. && \  
rm -r rdiffweb-* && \  
rm rdiffweb.tar.gz  
  
VOLUME /config /backups /restores /etc/rdiffweb  
  
EXPOSE 8080  
  
CMD ["/usr/bin/rdiffweb"]  
  

