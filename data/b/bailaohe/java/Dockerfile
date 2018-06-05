FROM debian  
MAINTAINER He Bai <bai.he@outlook.com>  
RUN apt-get update && apt-get install -y curl  
RUN curl -SL https://www.reucon.net/cdn/java/jdk-7u76-linux-x64.tar.gz | tar
-xzC /opt/  
RUN curl -SL
http://mirrors.hust.edu.cn/apache/maven/maven-3/3.3.3/binaries/apache-
maven-3.3.3-bin.tar.gz | tar -xzC /opt/  
WORKDIR /opt  
ENV JAVA_HOME /opt/jdk1.7.0_76  
ENV MAVEN_OPTS "-Xms256m -Xmx512m"  
ENV PATH ${JAVA_HOME}/bin:/opt/apache-maven-3.3.3/bin:${PATH}  
RUN echo ${PATH}  
  

