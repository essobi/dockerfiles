FROM maven:3.3.3-jdk-8  
MAINTAINER Jose Betanzos <gilberto.betanzos@gmail.com>  
  
RUN cd ~ && wget
https://repository.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/3.5.0/mule-standalone-3.5.0.tar.gz  
RUN cd /opt && tar xvzf ~/mule-standalone-3.5.0.tar.gz && rm ~/mule-
standalone-3.5.0.tar.gz && ln -s /opt/mule-standalone-3.5.0 /opt/mule  
  
ENV MULE_HOME /opt/mule  
  
VOLUME ["/opt/mule/logs", "/opt/mule/conf", "/opt/mule/apps",
"/opt/mule/domains"]  
  
WORKDIR /opt/mule  
  
CMD [ "/opt/mule/bin/mule" ]  
  
EXPOSE 8083  

