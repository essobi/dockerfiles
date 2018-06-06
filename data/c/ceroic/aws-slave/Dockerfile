FROM ceroic/docker-slave:1.11.2  
MAINTAINER Ceroic <ops@ceroic.com>  
  
RUN \  
apt-get update && \  
apt-get install -y \  
build-essential \  
bzip2 \  
ca-certificates \  
daemontools \  
libssl-dev \  
python-dev \  
python-setuptools && \  
easy_install pip && \  
pip install --upgrade setuptools && \  
pip install awscli  
  
# Install AWS ECS CLI  
RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-
cli/ecs-cli-linux-amd64-latest  
RUN chmod +x /usr/local/bin/ecs-cli

