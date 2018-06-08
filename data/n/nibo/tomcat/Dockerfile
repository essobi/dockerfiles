FROM nibo/oracle-jdk:jre-8u112  
MAINTAINER Richard <nibocn@gmail.com>  
  
ENV TOMCAT_MAJOR=8 \  
TOMCAT_VERSION=8.5.11 \  
CATALINA_HOME=/opt/tomcat \  
TZ=Asia/Shanghai  
  
ENV PATH=$CATALINA_HOME/bin:$PATH  
  
RUN cd /tmp \  
&& curl -o tomcat.tar.gz
http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz \  
&& tar xf tomcat.tar.gz -C /opt \  
&& rm tomcat.tar.gz \  
&& mv /opt/apache-tomcat* /opt/tomcat \  
&& rm -rf /opt/tomcat/webapps/* \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& echo $TZ > /etc/timezone  
  
COPY server.xml /opt/tomcat/conf  
  
WORKDIR /opt/tomcat  
  
EXPOSE 8080  
ENV RESERVED_MEGABYTES 64  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
CMD ["/entrypoint.sh"]  

