# radiantbluetechnologies/rialto-cesiumserver  
FROM radiantbluetechnologies/rialto-cesium  
MAINTAINER mpg@flaxen.com  
  
EXPOSE 8080  
COPY build.sh /tmp/  
RUN /tmp/build.sh  
  
COPY nginx.conf /etc/nginx/  
  
CMD nginx  

