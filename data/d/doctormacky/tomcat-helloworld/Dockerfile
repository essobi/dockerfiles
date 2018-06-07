FROM tomcat:8.0.20-jre8  
MAINTAINER liuyun105@126.com  
RUN set -x \  
\  
&& rm -rf /usr/local/tomcat/webapps/ROOT/* \  
&& mkdir /usr/local/tomcat/macky \  
&& wget -P /usr/local/tomcat/macky http://7xox9v.com1.z0.glb.clouddn.com/qx-
console.war \  
&& unzip -o /usr/local/tomcat/macky/qx-console.war -d
/usr/local/tomcat/webapps/ROOT/ \  
&& rm -rf /usr/local/tomcat/macky  
  
CMD ["catalina.sh", "run"]

