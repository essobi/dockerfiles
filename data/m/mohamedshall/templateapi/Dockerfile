FROM centos  
ENV JAVA_VERSION 8u31  
ENV BUILD_VERSION b13  
  
# Upgrading system  
RUN yum -y upgrade  
RUN yum -y install wget  
  
# Downloading & Config Java 8  
RUN wget -c --header "Cookie: oraclelicense=accept-securebackup-cookie"
"http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.rpm"
-O /tmp/jdk-8u131-linux-x64.rpm  
#RUN gunzip jdk-8u131-linux-x64.tar.gz  
RUN yum -y install /tmp/jdk-8u131-linux-x64.rpm  
#RUN alternatives --install /usr/bin/java jar /usr/java/latest/bin/java 200000  
#RUN alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws
200000  
#RUN alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac
200000  
EXPOSE 7001  
VOLUME /tmp  
ADD /maven/Template-0.0.1-SNAPSHOT.jar template.jar  
RUN sh -c 'touch /template.jar'  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/template.jar"]

