FROM centos  
ENV JAVA_VERSION 8u151  
ENV BUILD_VERSION b13  
# Upgrading system  
RUN yum -y upgrade  
RUN yum -y install wget maven  
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
EXPOSE 8081  
#install Spring Boot artifact  
USER 1000050000  
VOLUME /tmp  
ADD target/cecl-fileupload-service.jar cecl-fileupload-service.jar  
RUN sh -c 'touch cecl-fileupload-service.jar'  
ENTRYPOINT ["java",
"-Dspring.data.mongodb.uri=mongodb://cecl:cecl@18.221.202.202/loans",
"-jar","cecl-fileupload-service.jar"]

