FROM jenkins:1.651.3  
LABEL maintainer "Backend Team <backend@socialpoint.es>"  
  
USER root  
  
RUN printf "\nexport TERM=xterm" >> /etc/bash.bashrc \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install \  
sudo \  
nano \  
build-essential \  
apt-utils \  
python-pip \  
python-dev \  
libssl-dev \  
libffi-dev \  
groovy \  
ssh \  
rsync \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
software-properties-common \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python  
  
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add - \  
&& echo "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-
release; echo $ID) $(lsb_release -cs) stable" >
/etc/apt/sources.list.d/docker.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install \  
docker-ce \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV DOCKER_COMPOSE 1.18.0  
RUN curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE}/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \  
&& chmod 755 /usr/local/bin/docker-compose  
  
RUN usermod -aG jenkins jenkins \  
&& echo "jenkins ALL=(ALL:ALL) NOPASSWD:ALL" > /etc/sudoers.d/jenkins

