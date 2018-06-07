FROM ubuntu:16.04  
ENV TOOL_VER_DOCKER="17.06.2"  
RUN apt-get update -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
openssh-server \  
curl \  
&& mkdir -p $HOME/.ssh \  
&& mkdir -p /var/run/sshd  
  
# Install docker  
# as described at: https://docs.docker.com/engine/installation/linux/ubuntu/  
# For available docker-ce versions  
# you can run `sudo apt-get update && sudo apt-cache policy docker-ce`  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
apt-transport-https \  
ca-certificates \  
software-properties-common  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
RUN add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \  
&& DEBIAN_FRONTEND=noninteractive apt-get update -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-cache policy docker-ce \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
docker-ce=${TOOL_VER_DOCKER}~ce-0~ubuntu  
  
CMD ["/usr/sbin/sshd", "-D"]  

