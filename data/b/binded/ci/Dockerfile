FROM ubuntu:17.10  
ENV DEBIAN_FRONTEND=noninteractive  
ENV DOCKER_VERSION 17.05.0-ce  
ENV DOCKER_COMPOSE_VERSION 1.13.0  
RUN apt-get update -y && \  
apt-get install -y \  
build-essential \  
zip \  
curl \  
automake \  
wget \  
git \  
jq \  
python-pip && \  
rm -rf /var/lib/apt/lists/*  
  
# Install docker  
RUN mkdir -p /tmp/docker && \  
cd /tmp/docker && \  
wget https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz
&& \  
tar -xzf *.tgz && \  
mv docker/* /usr/local/bin/ && \  
rm -rf /tmp/docker  
  
# Install docker-compose  
RUN wget \  
-O /usr/local/bin/docker-compose \  
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-Linux-x86_64  
RUN chmod u+x /usr/local/bin/docker-compose  
  
# Install aws cli  
RUN pip install -U pip && \  
pip install awscli  
  
# Installs terraform, helm, kops and kubectl  
RUN curl "https://raw.githubusercontent.com/binded/scripts/master/install-cli-
tools.sh" \  
| bash  
  
# Init helm  
RUN helm init --client-only  
  
# Install sentry CLI  
RUN curl -sL https://sentry.io/get-cli/ | bash  
  
WORKDIR /ci/project  
  
COPY ./rootfs /  
  
ENV PATH /ci/bin:$PATH  

