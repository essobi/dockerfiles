FROM ubuntu  
MAINTAINER Yusuf Ali "ali@yusuf.email"  
RUN \  
apt-get update && apt-get install -y vim tmux sudo python python-pip git curl
build-essential gnupg2 && \  
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - && \  
sudo apt-get install -y nodejs && \  
useradd yusuf -d /home/yusuf -s /bin/bash && \  
usermod -aG sudo yusuf && \  
/usr/bin/npm install -g gulp react react-dom && \  
echo "yusuf ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
USER yusuf  
VOLUME /home/yusuf  
ENTRYPOINT ["/bin/bash"]  

