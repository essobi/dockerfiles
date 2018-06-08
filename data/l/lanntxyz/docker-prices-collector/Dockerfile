# create image from java  
FROM java:alpine  
  
EXPOSE 80 443  
VOLUME ["/opt/prices-collector", "/opt/script", "/bin/bash"]  
  
# add jar to docker  
# ADD ./script /opt/script  
# set environment variable  
# ENV JAVA_OPTS=""  
RUN chmod +x /bin/bash  
RUN chmod +x /opt/script  
RUN chmod 777 /opt/prices-collector  

