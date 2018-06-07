FROM openjdk:8-jre-alpine  
MAINTAINER mr5.simple@gmail.com  
  
RUN apk add -U tzdata bash file  
  
RUN mkdir -p /opt/otter_manager  
ADD
https://github.com/alibaba/otter/releases/download/v4.2.14/manager.deployer-4.2.14.tar.gz
/opt/otter_manager/  
RUN cd /opt/otter_manager && tar -zxvf manager.deployer-4.2.14.tar.gz && rm
manager.deployer-4.2.14.tar.gz  
  
ADD docker-entrypoint.sh /  
RUN chmod +x docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

