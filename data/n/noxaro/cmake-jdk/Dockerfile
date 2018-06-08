FROM debian:9  
MAINTAINER Noxaro<github@demofire.de>  
  
RUN echo "deb http://deb.debian.org/debian stretch main\n deb-src
http://deb.debian.org/debian stretch main\n deb
http://security.debian.org/debian-security stretch/updates main\n deb-src
http://security.debian.org/debian-security stretch/updates main" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y install openjdk-8-jdk cmake gcc build-essential wget unzip  
RUN mkdir /sonarqube  
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-3.0.3.778-linux.zip -P /sonarqube  
RUN wget https://sonarcloud.io/static/cpp/build-wrapper-linux-x86.zip -P
/sonarqube  
RUN unzip /sonarqube/build-wrapper-linux-x86.zip -d /sonarqube  
RUN unzip /sonarqube/sonar-scanner-cli-3.0.3.778-linux.zip -d /sonarqube  
  
ENV PATH="/sonarqube/build-wrapper-linux-x86/:/sonarqube/sonar-
scanner-3.0.3.778-linux/bin:${PATH}"  

