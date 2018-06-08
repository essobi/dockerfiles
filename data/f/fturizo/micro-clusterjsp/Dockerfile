FROM payara/micro  
MAINTAINER fturizo  
  
ADD hazelcast.xml ./hazelcast.xml  
ENV APP_LOCATION ./deployments/clusterjsp.war  
ENV INTERFACE_NETWORK 10.0.1.*  
ENV INTERFACE_RANGE 10.0.1.0-10  
RUN wget -O $APP_LOCATION
https://community.jboss.org/servlet/JiveServlet/download/588259-27006/clusterjsp.war  
  
EXPOSE 5700  
ENTRYPOINT java -jar -Dinterface.network=$INTERFACE_NETWORK
-Dinterface.range=$INTERFACE_RANGE payara-micro.jar --deploy $APP_LOCATION
\--hzConfigFile ./hazelcast.xml  

