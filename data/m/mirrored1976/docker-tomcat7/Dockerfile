FROM java:7-jre-alpine  
  
MAINTAINER takeshi.hirosue@bigtreetc.com  
  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.70  
ENV TOMCAT7 apache-tomcat-${TOMCAT_VERSION}  
ENV TOMCAT_URL
http://ftp.meisei-u.ac.jp/mirror/apache/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/${TOMCAT7}.tar.gz  
  
RUN wget ${TOMCAT_URL} \  
&& tar xvfz ${TOMCAT7}.tar.gz \  
&& rm ${TOMCAT7}/bin/*bat \  
&& rm ${TOMCAT7}.tar.gz \  
&& rm ${TOMCAT7}/bin/*.tar.gz  
  
EXPOSE 8080  
CMD ["/apache-tomcat-7.0.70/bin/catalina.sh", "run"]  

