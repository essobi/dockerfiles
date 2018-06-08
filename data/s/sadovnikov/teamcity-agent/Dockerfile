FROM sadovnikov/container-base:0.1  
MAINTAINER Viktor Sadovnikov <viktor@jv-ration.com>  
  
ADD setup-agent.sh /setup-agent.sh  
RUN adduser teamcity  
  
EXPOSE 9090  
CMD sudo -u teamcity -s -- sh -c
"TEAMCITY_SERVER=http://${TC_SERVER_PORT_8111_TCP_ADDR}:${TC_SERVER_PORT_8111_TCP_PORT}
bash /setup-agent.sh run"  

