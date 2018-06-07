FROM tomcat:8  
MAINTAINER Romulo Rodríguez rodriguezrjrr@gmail.com  
  
RUN wget
http://downloads.sourceforge.net/project/jasperserver/JasperServer/JasperReports%20Server%20Community%20Edition%206.3.0/jasperreports-
server-cp-6.3.0-bin.zip -O /tmp/jasperreports-server-cp-6.3.0-bin.zip  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN chmod a+x /docker-entrypoint.sh  
  
ENV JAVA_OPTS="-Xms1024m -Xmx2048m -XX:PermSize=32m -XX:MaxPermSize=512m
-Xss2m -XX:+UseConcMarkSweepGC -XX:+CMSClassUnloadingEnabled"  
ENTRYPOINT ["/docker-entrypoint.sh"]

