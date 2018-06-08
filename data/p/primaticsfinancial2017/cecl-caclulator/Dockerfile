FROM centos  
ENV JAVA_VERSION 8u151  
ENV BUILD_VERSION b13  
# Upgrading system  
RUN yum -y upgrade  
RUN yum -y install wget  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.rpm"
-O /tmp/jdk-8-linux-x64.rpm  
RUN yum -y install /tmp/jdk-8-linux-x64.rpm  
RUN alternatives --install /usr/bin/jar jar /usr/java/latest/bin/java 200000  
RUN alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws
200000  
RUN alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac
200000  
ENV JAVA_OPTS -XX:+UseG1GC -XX:+UseTLAB -XX:NewSize=512m -XX:MaxNewSize=512m
-XX:MaxTenuringThreshold=0 -XX:SurvivorRatio=1024
-XX:+UseCMSInitiatingOccupancyOnly -XX:CMSInitiatingOccupancyFraction=60
-Xss16m  
EXPOSE 8084  
VOLUME ["/data"]  
ENTRYPOINT ["java",
"-Dspring.data.mongodb.uri=mongodb://cecl:cecl@18.221.202.202/loans",
"-jar","cecl-ignite-cache-service.jar"]

