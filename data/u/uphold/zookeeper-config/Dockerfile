FROM rancher/confd-base:0.11.0-dev-rancher  
  
COPY ./conf.d /etc/confd/conf.d  
COPY ./log4j.properties /opt/zookeeper/conf/  
COPY ./templates /etc/confd/templates  
  
VOLUME /opt/zookeeper/conf  
VOLUME /tmp/zookeeper  
  
ENTRYPOINT ["/confd"]  
CMD ["--backend", "rancher", "--prefix", "/2015-12-19", "--interval", "10"]  

