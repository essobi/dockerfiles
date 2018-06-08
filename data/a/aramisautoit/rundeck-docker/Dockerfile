FROM jordan/rundeck  
  
# Docker installation  
RUN apt-get -y update \  
&& apt-get -y install apt-transport-https ca-certificates \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list \  
&& apt-get -y update \  
&& apt-get -y install docker-engine \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Make sure rundeck can start and communicate with docker daemon  
RUN usermod -a -G sudo rundeck && \  
echo "rundeck ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/50_rundeck  

