FROM jenkinsci/jenkins:2.0-rc-1  
USER root  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN apt-get update \  
&& apt-get -y install apt-transport-https make \  
&& apt-get clean  
RUN echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list  
RUN apt-get update \  
&& apt-get -y install docker-engine=1.9.1-0~jessie \  
&& apt-get clean  
RUN usermod -G docker jenkins  
  

