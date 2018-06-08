FROM ubuntu:14.04  
RUN sed -i 's/\/\//\/\/ro./g' /etc/apt/sources.list &&\  
apt-get update &&\  
apt-get -y dist-upgrade &&\  
apt-get install -y git-core subversion build-essential &&\  
apt-get clean &&\  
useradd -m -s /bin/bash dev &&\  
(echo dev:dev | chpasswd) &&\  
echo 'dev ALL=NOPASSWD: ALL' > /etc/sudoers.d/dev  
  
ENTRYPOINT ["/usr/bin/sudo", "-iHu", "dev"]  

