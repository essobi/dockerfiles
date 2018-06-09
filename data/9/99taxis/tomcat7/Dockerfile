FROM 99taxis/oracle-java8  
MAINTAINER "Fabio Hisamoto" <fhisamoto@gmail.com>  
LABEL version="0.1"  
  
ENV TOMCATVER 7.0.64  
RUN \  
apt-get update && \  
apt-get install -y libtcnative-1 libapr1 libapr1-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /var/tmp/*  
  
RUN (\  
wget -O /tmp/tomcat7.tar.gz
http://archive.apache.org/dist/tomcat/tomcat-7/v$TOMCATVER/bin/apache-
tomcat-$TOMCATVER.tar.gz && \  
cd /opt && \  
tar zxf /tmp/tomcat7.tar.gz && \  
mv /opt/apache-tomcat* /opt/tomcat && \  
rm /tmp/tomcat7.tar.gz)  
  
RUN rm -rf\  
/opt/tomcat/webapps/docs \  
/opt/tomcat/webapps/examples \  
/opt/tomcat/webapps/ROOT \  
/opt/tomcat/webapps/host-manager \  
/opt/tomcat/webapps/manager  
  
RUN useradd -ms /bin/false tomcat  
RUN chown -R tomcat:tomcat /opt/tomcat  
  
COPY srv/etc/service/app/run_app.sh /etc/service/app/run  
RUN chmod +x /etc/service/app/run  
  
EXPOSE 8080  
ENTRYPOINT ["/sbin/my_init"]  

