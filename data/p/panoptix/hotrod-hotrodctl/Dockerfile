FROM ubuntu:14.04.4  
ENV REFRESHED_ON "12 June 2017"  
RUN apt-get update  
RUN apt-get install -y \  
curl \  
apt-transport-https \  
ca-certificates  
  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" >
/etc/apt/sources.list.d/docker.list  
RUN apt-get update  
  
RUN apt-get install -y docker-engine  
  
ADD hotrodctl /usr/bin/hotrodctl  
ENTRYPOINT ["/usr/bin/hotrodctl"]  
CMD ["supervise"]  

