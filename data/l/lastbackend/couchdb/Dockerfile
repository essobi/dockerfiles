FROM ubuntu:trusty  
  
MAINTAINER support@lastbackend.com  
  
# Setup curl dependency  
RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf
/var/lib/apt/lists  
  
#install CouchDB  
RUN apt-get update && \  
apt-get install -y couchdb pwgen && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /var/run/couchdb  
RUN sed -i -r 's/;bind_address = 127.0.0.1/bind_address = 0.0.0.0/'
/etc/couchdb/local.ini  
  
# Add scripts  
ADD init.sh /init.sh  
RUN chmod +x /*.sh  
  
EXPOSE 5984  
CMD ["/init.sh"]

