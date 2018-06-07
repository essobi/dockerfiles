  
# docker run -e TEAMCITY_SERVER=http://buildserver:8111 -dt -p 9090:9090
kornsn/centos7-teamcity-agent-base  
FROM kornsn/centos7-oracle-jre7  
  
MAINTAINER Sergei Korneev <Sergei_Korneev@epam.com>  
  
ADD setup-agent.sh /setup-agent.sh  
RUN yum -y install wget unzip sudo  
RUN adduser teamcity  
  
EXPOSE 9090  
CMD sudo -u teamcity -s -- sh -c "TEAMCITY_SERVER=$TEAMCITY_SERVER bash
/setup-agent.sh run"  

