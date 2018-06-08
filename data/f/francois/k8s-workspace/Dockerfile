# This Dockerfile deploy a keystone container :  
# based on ubuntu:14.04, it runs the keystone source code from branch
stable/icehouse  
# it has to be linked to a mysql container named db-keystone :  
# -  
#  
FROM ubuntu:14.04  
MAINTAINER Francois Billant <fbillant@gmail.com>  
  
EXPOSE 22  
RUN apt-get update && \  
apt-get -y install git ssh vim wget && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# install Kubecfg  
RUN wget http://storage.googleapis.com/kubernetes/kubecfg -O
/usr/local/bin/kubecfg && \  
chmod +x /usr/local/bin/kubecfg  
  
# Install docker to manage kubelets hosts through their docker-socket  
RUN wget https://get.docker.io/builds/Linux/x86_64/docker-1.2.0 -O /bin/docker
&& \  
chmod +x /bin/docker  
  
ADD . /config  
  
CMD cd /config && ./config.sh && ./run.sh  

