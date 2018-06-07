FROM greatbsky/xtraos:latest  
MAINTAINER architect.bian  
LABEL name="openjdkx" license="MIT" build-date="20180119"  
  
ENV VERSION 1.8.0.161  
ENV JAVA_HOME=/usr  
  
RUN yum update -y && cd /data/softs && yum install -y java  
  
CMD ["java", "-version"]  

