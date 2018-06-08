FROM jenkins/jenkins:2.109  
# Suppress apt installation warnings  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Change to root user  
USER root  
  
RUN apt-get update -y && \  
apt-get install \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
software-properties-common \  
python-dev \  
python-setuptools \  
python-pip \  
gcc \  
make \  
libssl-dev -y  
  
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add - && \  
apt-key fingerprint 0EBFCD88  
  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) \  
stable"  
  
# Used to set the docker group ID  
# Set to 497 by default, which is the group ID used by AWS Linux ECS Instance  
ARG DOCKER_GID=497  
# Create Docker Group with GID  
# Set default value if DOCKER_GID set to blank string by Docker Compose  
RUN groupadd -g ${DOCKER_GID:-497} docker  
  
# Control docker version  
ARG DOCKER_CE=17.12.0  
# Install  
RUN apt-get update -y && \  
apt-get install docker-ce=${DOCKER_CE:-17.12.0}~ce-0~debian -y  
  
# Control docker=compose version  
ARG DOCKER_COMPOSE=1.19.0  
# Install Docker Compose  
RUN pip install docker-compose==${DOCKER_COMPOSE:-1.19.0} && \  
pip install ansible boto boto3  
  
RUN usermod -aG staff jenkins && \  
usermod -aG docker jenkins  
  
# Change to jenkins user  
USER jenkins  
  
# Add Jenkins plugins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN xargs /usr/local/bin/install-plugins.sh < //usr/share/jenkins/plugins.txt

