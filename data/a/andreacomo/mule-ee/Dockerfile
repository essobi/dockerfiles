FROM java:openjdk-8-jdk  
  
MAINTAINER andrea.como@gmail.com  
  
RUN cd /opt && wget http://s3.amazonaws.com/new-mule-artifacts/mule-ee-
distribution-standalone-3.8.4.tar.gz  
  
RUN cd /opt && tar xvzf mule-ee-distribution-standalone-3.8.4.tar.gz && rm
mule-ee-distribution-standalone-3.8.4.tar.gz && ln -s /opt/mule-enterprise-
standalone-3.8.4 /opt/mule  
  
# Define environment variables.  
ENV MULE_HOME /opt/mule  
  
# Define mount points.  
VOLUME ["/opt/mule/logs", "/opt/mule/apps", "/opt/mule/domains"]  
  
# Define working directory.  
WORKDIR /opt/mule  
  
CMD [ "/opt/mule/bin/mule" ]  
  
# Default http port  
EXPOSE 8081  

