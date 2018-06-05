FROM cilliemalan/ubuntu-with-tools  
  
MAINTAINER Cillie Malan <cilliemalan@gmail.com>  
  
#create user for teamcity  
RUN useradd teamcity -s /bin/bash -m && sudo chown -R teamcity
/usr/lib/node_modules  
  
EXPOSE 9090  
ADD setup-agent.sh /setup-agent.sh  
  
CMD sudo -u teamcity -H -s -- sh -c "TEAMCITY_SERVER=$TEAMCITY_SERVER bash
/setup-agent.sh run"  

