FROM maven:3.5.0-jdk-8  
  
MAINTAINER Yiannis Mouchakis <gmouchakis@iit.demokritos.gr>  
  
RUN git clone https://bitbucket.org/dataengineering/rassp.git && \  
cd rassp && \  
git checkout feat-large-groups && \  
mvn clean package && \  
cd proto && \  
mvn dependency:copy-dependencies  
  
ADD application.conf /root/application.conf  
ADD truststore.jks /root/truststore.jks  
ADD conf.sh /usr/bin  
  
EXPOSE 2552  
  
CMD conf.sh && cd /rassp/proto/target && java -cp "rassp-
proto-0.0.1-SNAPSHOT.jar:dependency/*" -Ddb.file=/root/dbFiles/User.json
-Dconfig.file=/root/application.conf
gr.demokritos.iit.radio.home.protocols.RASSP  

