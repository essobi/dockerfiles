FROM bitnami/minideb-extras:stretch  
  
ENV DOCKER_VER="17.09.1~ce-0~debian"  
ENV COMPOSE_VER="1.17.0"  
  
RUN sudo apt-get update \  
&& install_packages \  
apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common \  
&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add
\- \  
&& sudo apt-key fingerprint 0EBFCD88 \  
&& sudo add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) \  
stable" \  
&& sudo apt-get update \  
&& install_packages python python-pip \  
git \  
ssh \  
unzip  
  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" \  
&& unzip awscli-bundle.zip \  
&& ./awscli-bundle/install -i /usr/local/aws -b /usr/bin/aws \  
&& install_packages docker-ce=$DOCKER_VER \  
&& curl -L
https://github.com/docker/compose/releases/download/${COMPOSE_VER}/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \  
&& sudo chmod +x /usr/local/bin/docker-compose  

