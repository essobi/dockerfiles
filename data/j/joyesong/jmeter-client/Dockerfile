# Use vinsdocker base image  
FROM joyesong/jmeter4.0-base  
MAINTAINER joyesong@qq.com  
  
# Ports to be exposed from the container for JMeter Master  
EXPOSE 60000  
COPY run.sh /run.sh  
RUN ["chmod", "+x", "/run.sh"]  
COPY hostkey /hostkey  
RUN chmod 600 /hostkey  
COPY dev2-login.jmx /  
WORKDIR /  
  
CMD ["bash", "/run.sh"]  

