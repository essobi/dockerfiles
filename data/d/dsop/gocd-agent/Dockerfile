FROM gocd/gocd-agent  
RUN apt-get update  
RUN apt-get -y install apt-transport-https ca-certificates  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" >
/etc/apt/sources.list.d/docker.list  
RUN apt-get update  
RUN apt-get -y install docker-engine  
RUN usermod -a -G docker go  
RUN mkdir /etc/service/docker  
RUN echo "#!/bin/bash" > /etc/service/docker/run  
RUN echo "docker daemon" >> /etc/service/docker/run  
RUN chmod +x /etc/service/docker/run  
RUN apt-get -y install jq  
RUN apt-get -y install gettext  

