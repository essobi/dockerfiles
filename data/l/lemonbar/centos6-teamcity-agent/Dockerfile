# docker run -e TEAMCITY_SERVER=http://buildserver:8111 -e AGENT_NAME=agent01
-dt -p 9090:9090 ariya/centos6-teamcity-agent  
FROM ariya/centos6-oracle-jre7  
  
MAINTAINER lemonbar <limengabc@163.com>  
  
ADD setup-agent.sh /setup-agent.sh  
RUN yum -y install wget unzip sudo  
RUN adduser teamcity  
  
EXPOSE 9090  
CMD sudo -u teamcity -s -- sh -c "TEAMCITY_SERVER=$TEAMCITY_SERVER
AGENT_NAME=$AGENT_NAME bash /setup-agent.sh run"  

