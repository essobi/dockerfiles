FROM java:8  
MAINTAINER Cesar Salazar <csalazar@devsu.com>  
  
RUN apt-get update \  
&& apt-get install -y sudo build-essential rsync \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN useradd -ms /bin/bash teamcity  
ADD start-agent.sh /start-agent.sh  
  
WORKDIR /home/teamcity  
VOLUME /home/teamcity  
  
EXPOSE 9090  
CMD su - teamcity -c "TEAMCITY_SERVER=$TEAMCITY_SERVER bash /start-agent.sh
run"  

