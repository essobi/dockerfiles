FROM anapsix/alpine-java:jdk8  
MAINTAINER Florian Brüssel <florian@florian-m.net>  
  
#add openssl for https download  
RUN apk add --update openssl && \  
rm -rf /var/cache/apk/* /tmp/*  
  
# set version info for desired tomcat version  
ENV TC_MAJOR 6  
ENV TC_VERSION 6.0.53  
# calculate download url  
ENV TC_URL
https://archive.apache.org/dist/tomcat/tomcat-$TC_MAJOR/v$TC_VERSION/bin/apache-
tomcat-$TC_VERSION.tar.gz  
  
# download and verify tomcat  
WORKDIR /opt  
RUN wget $TC_URL && \  
wget $TC_URL.sha1 && \  
sha1sum -cw apache-tomcat-$TC_VERSION.tar.gz.sha1  
  
# install tomcat to /opt/apache-tomcat  
RUN tar -xzf apache-tomcat-$TC_VERSION.tar.gz && \  
mv apache-tomcat-$TC_VERSION apache-tomcat  
  
# remove unnecessary components  
RUN rm -f apache-tomcat/bin/*.bat && \  
rm -rf apache-tomcat/webapps/docs && \  
rm -rf apache-tomcat/webapps/examples && \  
rm -rf apache-tomcat/webapps/manager && \  
rm -rf apache-tomcat/webapps/host-manager && \  
rm -f apache-tomcat-$TC_VERSION.*  
  
#improve tomcat startup performance by setting non blocking random generator  
RUN echo "CATALINA_OPTS=-Djava.security.egd=file:/dev/./urandom" > apache-
tomcat/bin/setenv.sh && \  
chmod a+x apache-tomcat/bin/setenv.sh  
  
WORKDIR /opt/apache-tomcat  
  
# add volume for webapps folder  
VOLUME /opt/apache-tomcat/webapps  
  
# expose http and jmx ports  
EXPOSE 8080 8009  
# run tomcat by default  
CMD ["/opt/apache-tomcat/bin/catalina.sh", "run"]  

