FROM tomcat:8  
  
MAINTAINER Yiannis Mouchakis <gmouchakis@iit.demokritos.gr>  
  
COPY . /opt/fedx-server  
  
RUN apt-get update && apt-get install -y git openjdk-7-jdk maven && \  
cd /opt/fedx-server && \  
mvn clean package && \  
cp target/fedx-*.war /usr/local/tomcat/webapps/ && \  
cd / && rm -r /opt/fedx-server && rm -r /root/.m2 && \  
apt-get \--purge remove -y git openjdk-7-jdk maven && apt-get \--purge
autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8080  
  
CMD catalina.sh run  

