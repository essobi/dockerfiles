FROM ubuntu:16.04  
RUN apt update -y && \  
apt upgrade -y && \  
apt install -y \  
ca-certificates \  
wget curl \  
software-properties-common \  
apt-transport-https \  
vim nano  
# && \  
# apt-get clean && \  
# rm -rf /var/lib/apt/lists/*  
# Install Docker and Compose  
RUN \  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \  
add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable" && \  
apt update && \  
apt install -y docker-ce && \  
curl -L https://github.com/docker/compose/releases/download/1.13.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
# Install GitLab's Runner  
RUN \  
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-ci-
multi-runner/script.deb.sh | bash && \  
apt update && \  
apt install -y gitlab-ci-multi-runner && \  
mkdir /scripts  
  
COPY scripts/up.sh /scripts/  
COPY scripts/exec.sh /scripts/  

