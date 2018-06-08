FROM sunhawk2100/linksamehub:v1.2  
MAINTAINER Levon.yao <levon.yao@linksame.cn>, Linksame Team  
  
# Patch APK Mirror to LINKSAME  
RUN echo "http://mirrors.ustc.edu.cn/alpine/v3.3/main/" >
/etc/apk/repositories  
  
COPY server.xml /opt/apache-tomcat/conf/  
  
EXPOSE 80  
# run tomcat by default  
CMD ["/opt/apache-tomcat/bin/catalina.sh", "run"]  

