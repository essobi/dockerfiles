  
# docker run -e TEAMCITY_SERVER=http://buildserver:8111 -dt -p 9090:9090
kornsn/centos7-teamcity-agent-docker  
FROM kornsn/centos7-teamcity-agent-base  
  
MAINTAINER Sergei Korneev <Sergei_Korneev@epam.com>  
  
RUN yum -y install docker  
ENTRYPOINT docker -d  

