FROM java:8-jre  
  
RUN apt-get update  
RUN cd /opt && \  
wget
https://repository.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/3.9.0/mule-standalone-3.9.0.tar.gz && \  
tar xvzf mule-standalone-3.9.0.tar.gz && \  
rm /opt/mule-standalone-3.9.0.tar.gz  
RUN ln -s /opt/mule-standalone-3.9.0 /opt/mule-standalone  
EXPOSE 8081  
CMD [ "/opt/mule-standalone/bin/mule" ]  
  

