FROM debian:8.6  
RUN apt-get update && apt-get -y install apt-transport-https ca-certificates  
RUN echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D\  
&& apt-get update && apt-get -y install docker-engine  
RUN apt-get autoclean  

