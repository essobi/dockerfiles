FROM garland/mesosphere-docker-mesos-master  
  
MAINTAINER David Asabina <david@supr.nu>  
  
#RUN date +"%Y/%m/%d %H:%M.%S" >> /tmp/start.time  
RUN apt-get update && apt-get upgrade -y && apt-get -y install docker.io  
RUN apt-get clean  
RUN echo "alias docker='docker -H unix:///var/run/docker.sock'" >> ~/.bashrc  
#RUN docker --version >> /tmp/docker.version  
  
ENTRYPOINT ["mesos-slave"]  

