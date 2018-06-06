FROM maven:3-jdk-8  
MAINTAINER Dave Woodward <davidwoodwrd@hotmail.com>  
  
RUN wget -P /opt https://bintray.com/artifact/download/business/maven/flyway-
commandline-3.2.1-linux-x64.tar.gz && \  
cd /opt && \  
tar -xvf flyway-commandline-3.2.1-linux-x64.tar.gz && \  
rm flyway-commandline-3.2.1-linux-x64.tar.gz  
  
ENV PATH $PATH:/opt/flyway-3.2.1  

