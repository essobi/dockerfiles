FROM docker.io/ubuntu:trusty  
  
RUN apt-get update \  
&& apt-get install -y apt-transport-https ca-certificates \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 \  
&& echo "deb https://get.docker.com/ubuntu docker main" >
/etc/apt/sources.list.d/docker.list \  
&& apt-get update \  
&& apt-get install -y git ssh-client lxc-docker \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /var/discourse  
  
CMD ["/bin/bash"]  

