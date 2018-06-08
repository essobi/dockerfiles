FROM nhong/motech-autobuild:latest  
ADD . /opt/motech/  
RUN cd /opt/motech && mvn clean install  
RUN cp /opt/motech/platform/server/target/motech-platform-server.war
/tomcat/webapps  
ENV TOMCAT_PASS secr3t  
ENV JAVA_OPTS -Xms1024m -Xmx2048m -XX:MaxPermSize=1024m -XX:PermSize=1024m  

