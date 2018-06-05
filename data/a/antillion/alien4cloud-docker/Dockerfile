FROM ubuntu:14.04  
MAINTAINER Oliver Tupman <otupman@antillion.com>  
# Original maintainer: https://github.com/san-tak/dockerfile  
# setting proxy  
#ENV http_proxy http://xxx.xxx.xxx.xxx:8080  
#ENV https_proxy https://xxx.xxx.xxx.xxx:8080  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
  
RUN apt-get update && \  
apt-get install -y software-properties-common \  
python-software-properties && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
apt-get install -y oracle-java8-installer \  
wget && \  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN mkdir -p /opt/alien4cloud && \  
wget -q
"http://fastconnect.org/maven/service/local/artifact/maven/redirect?r=opensource&g=alien4cloud&a=alien4cloud-
dist&v=1.3.0&p=tar.gz&c=dist" \  
-O /root/alien4cloud-dist-1.3.0.tar.gz  
  
RUN tar -xvf /root/alien4cloud-dist-1.3.0.tar.gz --directory /opt  
  
#RUN wget -q
"http://fastconnect.org/maven/service/local/artifact/maven/redirect?r=opensource&g=alien4cloud&a=alien4cloud-
ui&v=1.3.0&p=war&c=standalone" -O /root/alien4cloud-1.3.0-standalone.war  
VOLUME /opt/alien4cloud-data  
VOLUME /root/config  
ADD config /opt/alien4cloud/config  
ADD start.sh /root/start.sh  
  
#CMD java -XX:MaxPermSize=512m -jar /root/alien4cloud-1.3.0-standalone.war
--spring.profiles.active=security-demo  
WORKDIR /opt/alien4cloud  
CMD /opt/alien4cloud/alien4cloud.sh  
EXPOSE 8088 8089

