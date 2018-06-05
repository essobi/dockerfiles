FROM ubuntu:14.04  
MAINTAINER san-tak  
  
# setting proxy  
#ENV http_proxy http://xxx.xxx.xxx.xxx:8080  
#ENV https_proxy https://xxx.xxx.xxx.xxx:8080  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
  
RUN apt-get update && \  
apt-get install -y default-jdk && \  
apt-get install -y wget && \  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN wget -q
"http://fastconnect.org/maven/service/local/artifact/maven/redirect?r=opensource&g=alien4cloud&a=alien4cloud-
ui&v=1.0.0&p=war&c=standalone" -O /root/alien4cloud-1.0.0-standalone.war  
  
CMD java -XX:MaxPermSize=512m -jar /root/alien4cloud-1.0.0-standalone.war
--spring.profiles.active=security-demo  

