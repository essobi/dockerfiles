FROM lauerbt/arduinodev  
  
MAINTAINER thomas@lauerbach.de  
  
ENV CONTAINER_VERSION 1.0  
ADD customisation /opt/customisation/  
  
RUN ["/opt/customisation/init.sh"]  
  
CMD ["/opt/arduino-1.8.5/arduino"]  

