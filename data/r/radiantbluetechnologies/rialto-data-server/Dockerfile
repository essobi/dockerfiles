# radiantbluetechnologies/rialto-data-server  
FROM radiantbluetechnologies/rialtobase-centos  
  
MAINTAINER mpg@flaxen.com  
  
ENV RIALTO_BRANCH=dev  
  
VOLUME /rialtodata  
EXPOSE 8080  
COPY ./build.sh /tmp/  
RUN /tmp/build.sh  
  
COPY nginx.conf /etc/nginx/  
  
# at run-time, we put the (imported) volume on the web  
CMD ln -s /rialtodata /opt/www && nginx  

