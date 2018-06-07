FROM shadowrobot/ubuntu-ros-indigo-build-tools:latest  
  
MAINTAINER "Shadow Robot's Software Team <software@shadowrobot.com>"  
  
LABEL Description="RAMCIP Libraries Build Image" Version="1.0"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Setup access to GitHub using Deploy key  
RUN mkdir /root/.ssh/  
ADD id_rsa /root/.ssh/id_rsa  
  
RUN echo "Setting up Git Access" && \  
chmod 600 /root/.ssh/id_rsa && \  
touch /root/.ssh/known_hosts && \  
ssh-keyscan github.com >> /root/.ssh/known_hosts && \  
  
echo "Setting up bash as default shell" && \  
rm /bin/sh && \  
ln -s /bin/bash /bin/sh && \  
  
echo "Getting source code" && \  
apt-get update && \  
apt-get install -y git && \  
git clone --depth 1 git@github.com:shadow-robot/ramcip.git
/root/workspace/src/ramcip && \  
  
echo "Run main installation script" && \  
/root/workspace/src/ramcip/deployment/ansible/deploy.sh -t deploy -h docker-
libraries && \  
  
echo "Removing cache and files" && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.ssh && \  
rm -rf /root/workspace/src/ramcip  

