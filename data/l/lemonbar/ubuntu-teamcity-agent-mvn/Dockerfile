FROM jamesdbloom/docker-java7-maven  
  
MAINTAINER Lemon Bar "limengabc@163.com"  
RUN apt-get install -y unzip sudo  
ADD setup-agent.sh /setup-agent.sh  
RUN chmod 755 /setup-agent.sh  
RUN adduser --disabled-login --gecos GECOS teamcity  
RUN passwd -d teamcity  
  
EXPOSE 9090  
CMD sudo -u teamcity -H /setup-agent.sh $TEAMCITY_SERVER $AGENT_NAME  

