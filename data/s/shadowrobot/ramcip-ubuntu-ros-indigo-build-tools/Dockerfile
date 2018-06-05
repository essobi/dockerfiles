FROM shadowrobot/ramcip:libraries  
  
MAINTAINER "Shadow Robot's Software Team <software@shadowrobot.com>"  
LABEL Description="RAMCIP Project Build Image" Version="1.0"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Setup access to GitHub using Deploy key  
RUN mkdir /root/.ssh/  
ADD id_rsa /root/.ssh/id_rsa  
  
RUN echo "Setting up Git Access" && \  
chmod 600 /root/.ssh/id_rsa && \  
touch /root/.ssh/known_hosts && \  
ssh-keyscan github.com >> /root/.ssh/known_hosts && \  
  
echo "Getting source code" && \  
apt-get update && \  
apt-get install -y git && \  
git clone --depth 1 git@github.com:shadow-robot/ramcip.git
/home/user/workspace/src/ramcip && \  
chown -R user:user /home/user/workspace/src/ramcip && \  
  
echo "Run main installation script" && \  
gosu user /home/user/workspace/src/ramcip/deployment/ansible/deploy.sh -t
deploy -h docker && \  
  
echo "Removing cache" && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.ssh && \  
rm -rf /home/user/workspace/src/ramcip  

