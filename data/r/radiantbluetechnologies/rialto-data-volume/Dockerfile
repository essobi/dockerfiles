# radiantbluetechnologies/rialto-data-volume  
FROM radiantbluetechnologies/rialtobase-centos  
MAINTAINER mpg@flaxen.com  
  
ENV RIALTO_BRANCH=dev  
  
VOLUME /rialtodata  
EXPOSE 8080  
COPY ./build.sh /tmp/  
RUN /tmp/build.sh  
  
# at run-time, we populate the (exported) volume  
CMD rm -rf /rialtodata/* && cp -r /opt/data/* /rialtodata/  

