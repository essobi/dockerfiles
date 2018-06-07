FROM ubuntu:16.04  
MAINTAINER Qiang Li <lqecnu@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y libapr1-dev libssl-dev make gcc software-properties-
common python-software-properties curl openjdk-8-jdk  
# This is to update the ssl version. Tomcat 8 requires openssl 1.0.2  
RUN add-apt-repository ppa:0k53d-karl-f830m/openssl -y  
  
RUN apt-get install openssl  
# Download and unzip tomcat.  
RUN cd /opt \  
&& curl http://www-eu.apache.org/dist/tomcat/tomcat-8/v8.5.16/bin/apache-
tomcat-8.5.16.tar.gz \  
| tar xz  
# Unzip the apr native library source code.  
RUN cd /opt/apache-tomcat-8.5.16/bin \  
&& tar zxvf tomcat-native.tar.gz  
  
# Configure and make  
RUN cd /opt/apache-tomcat-8.5.16/bin/tomcat-native-1.2.12-src/native \  
&& ./configure --with-java-home=/usr/lib/jvm/java-8-openjdk-amd64
--prefix=/opt/apache-tomcat-8.5.16/bin \  
&& make && make install  
  
# Remove the source code.  
RUN cd /opt/apache-tomcat-8.5.16/bin && rm -r tomcat-native-1.2.12-src  
  
COPY ssl.cfg /opt/apache-tomcat-8.5.16/conf  
COPY server.xml /opt/apache-tomcat-8.5.16/conf/server.xml  
RUN cd /opt/apache-tomcat-8.5.16/conf \  
&& openssl req -x509 -newkey rsa:4096 -config ssl.cfg -keyout key.pem -out
cert.pem -days 365 -nodes  
  
ENV LD_LIBRARY_PATH=/opt/apache-tomcat-8.5.16/bin/lib  
EXPOSE 8443  
CMD ["/opt/apache-tomcat-8.5.16/bin/catalina.sh", "run"]  

