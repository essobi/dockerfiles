FROM debian:stretch-slim  
  
RUN bash -c 'mkdir -p /usr/share/man/man{1..8}' && \  
apt-get update && \  
apt-get install -y \--no-install-recommends openjdk-8-jdk-headless maven tree
git bzip2 wget gnupg apt-transport-https && \  
wget -qO - https://download.docker.com/linux/debian/gpg | apt-key add \- && \  
echo "deb [arch=amd64] https://download.docker.com/linux/debian stretch
stable" >> /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y \--no-install-recommends docker-ce && \  
apt-get purge -y wget gnupg apt-transport-https && \  
apt-get clean && \  
rm -rf /usr/share/man/* && \  
mkdir -p /data/db && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
  
ENV DOCKER_HOST="tcp://docker:2375"  

