# radiantbluetechnologies/rialto-gpkgserver  
FROM radiantbluetechnologies/rialtobase-centos  
MAINTAINER mpg@flaxen.com  
  
ENV RIALTO_BRANCH=dev  
  
VOLUME /rialtodata  
EXPOSE 8080  
RUN true  
  
COPY geopackage_server.py /usr/local/bin/  
  
CMD /usr/local/bin/geopackage_server.py 8080 /rialtodata  

