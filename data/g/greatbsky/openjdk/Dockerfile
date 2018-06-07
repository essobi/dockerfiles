FROM greatbsky/centos7:latest  
MAINTAINER architect.bian  
LABEL name="openjdk" license="MIT" build-date="20180119"  
  
ENV VERSION 1.8.0_161  
ENV JAVA_HOME=/usr  
  
RUN yum update -y && cd /data/softs && yum install -y java  
  
CMD ["java", "-version"]  

