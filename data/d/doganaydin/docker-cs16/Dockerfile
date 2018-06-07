FROM ubuntu:latest  
  
MAINTAINER Doğan Aydın <dogan1aydin@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y git-core  
RUN git clone https://gitorious.org/cs16-docker/cs16-docker.git  
CMD ./cs16-docker/hlds_run -binary ./cs16-docker/hlds_amd -game cstrike +map
de_dust2 +maxplayers 30 -nomaster -insecure +sys_ticrate 250 +sv_lan 1  
  
EXPOSE 27015 27015  
EXPOSE 27039 27039  
EXPOSE 1200/udp 1200/udp  
EXPOSE 27000/udp 27000/udp  
EXPOSE 27015/udp 27015/udp

