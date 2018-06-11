FROM klaemo/couchdb-base  
  
MAINTAINER Clemens Stolle klaemo@fastmail.fm  
  
# Get the source  
RUN cd /opt && \  
wget https://dist.apache.org/repos/dist/dev/couchdb/source/1.6.1/rc.4/apache-
couchdb-1.6.1.tar.gz && \  
tar xzf /opt/apache-couchdb-*  
  
# build couchdb  
RUN cd /opt/apache-couchdb-* && ./configure && make && make install  
  
# cleanup  
RUN apt-get remove -y build-essential wget curl && \  
apt-get autoremove -y && apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /opt/apache-couchdb-*  
  
ADD ./opt /opt  
  
# Configuration  
RUN sed -e 's/^bind_address = .*$/bind_address = 0.0.0.0/' -i
/usr/local/etc/couchdb/default.ini  
RUN /opt/couchdb-config  
  
# Define mountable directories.  
VOLUME ["/usr/local/var/log/couchdb", "/usr/local/var/lib/couchdb",
"/usr/local/etc/couchdb"]  
  
EXPOSE 5984  
CMD ["/opt/start_couch"]  

