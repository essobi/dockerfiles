# Start from a Maven image.  
FROM maven:3-jdk-8  
# Ignite version  
ENV IGNITE_VERSION 1.9.0  
# Ignite home  
ENV IGNITE_HOME /opt/apache-ignite-fabric-${IGNITE_VERSION}-bin  
  
WORKDIR /opt  
  
RUN curl
https://dist.apache.org/repos/dist/release/ignite/${IGNITE_VERSION}/apache-
ignite-fabric-${IGNITE_VERSION}-bin.zip -o ignite.zip \  
&& unzip ignite.zip \  
&& rm ignite.zip  
  
RUN git clone https://github.com/orangeRat/test-ignite.git \  
&& cd test-ignite \  
&& mvn package \  
&& mv target/*.jar /opt/test-ignite.jar \  
&& mv scripts/run.sh /opt \  
&& cd /opt \  
&& rm -rf test-ignite \  
&& chmod +x /opt/run.sh  
  
CMD /opt/run.sh  
  
EXPOSE 8080  

