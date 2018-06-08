FROM tomcat:8  
  
MAINTAINER Yiannis Mouchakis <gmouchakis@iit.demokritos.gr>  
  
RUN apt-get update && apt-get install -y git openjdk-7-jdk maven && \  
cd /opt && \  
git clone https://github.com/semagrow/fork-splendid-server.git && \  
cd fork-splendid-server && \  
git checkout mavenize && \  
mvn clean package -P server && \  
cd /opt/fork-splendid-server && \  
cp target/splendid-*.war /usr/local/tomcat/webapps/ && \  
cd / && rm -r /opt/fork-splendid-server && rm -r /root/.m2 && \  
apt-get \--purge remove -y git openjdk-7-jdk maven && apt-get \--purge
autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8080  
  
CMD catalina.sh run  

