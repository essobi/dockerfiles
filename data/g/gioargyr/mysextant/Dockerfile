FROM ubuntu:14.04  
MAINTAINER George Papadakis <gpapadis@di.uoa.gr>  
  
ENV PORT 8080  
ENV TOMCAT_MAJOR_VERSION 7  
ENV TOMCAT_MINOR_VERSION 7.0.55  
RUN apt-get update && \  
apt-get install -y \  
default-jdk \  
maven \  
mercurial \  
wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# INSTALL TOMCAT  
RUN wget -q
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz && \  
wget -qO-
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c - && \  
tar zxf apache-tomcat-*.tar.gz && \  
rm apache-tomcat-*.tar.gz && \  
mv apache-tomcat* tomcat  
  
RUN hg clone http://hg.strabon.di.uoa.gr/Sextant-New -r testBD && \  
cd Sextant-New/JerseyServer&& \  
mvn clean package  
  
RUN cp /Sextant-New/JerseyServer/target/*.war /tomcat/webapps/Sextant_v2.0.war
&& \  
rm -Rf /Sextant-New  
  
ADD create_tomcat_admin_user.sh /create_tomcat_admin_user.sh  
ADD sextant.sh /sextant.sh  
RUN chmod +x /*.sh  
  
EXPOSE $PORT  
CMD ["/bin/bash", "/sextant.sh"]  

