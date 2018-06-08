FROM ubuntu:16.04  
  
# Get some packages  
RUN set -ex \  
&& apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https \  
ca-certificates \  
curl \  
dnsutils \  
git \  
htop \  
less \  
nodejs \  
npm \  
ssh \  
unzip \  
vim \  
# \  
# Clean up after apt \  
&& rm -rf /var/lib/apt/lists/* \  
# \  
# Link Node.js to the expected name \  
&& ln -s /usr/bin/nodejs /usr/bin/node  
  
# Install Triton-specific tools  
RUN set -ex \  
# Install Triton CLI and related tools \  
&& npm install -g triton manta json \  
# \  
# Install triton-docker CLI, from https://github.com/joyent/triton-docker-cli
\  
&& curl -o /usr/local/bin/triton-docker
https://raw.githubusercontent.com/joyent/triton-docker-cli/master/triton-
docker \  
&& chmod +x /usr/local/bin/triton-docker \  
&& ln -Fs /usr/local/bin/triton-docker /usr/local/bin/triton-compose \  
&& ln -Fs /usr/local/bin/triton-docker /usr/local/bin/triton-docker-install \  
&& ln -Fs /usr/local/bin/triton-docker-helper /usr/local/bin/docker \  
&& ln -Fs /usr/local/bin/triton-compose-helper /usr/local/bin/docker-compose \  
&& /usr/local/bin/triton-docker-install  
  
# Fetch some demo repos  
RUN set -ex \  
&& mkdir /demo \  
&& cd /demo \  
&& git clone https://github.com/autopilotpattern/prometheus.git  
WORKDIR /demo  
  
# Build meta and Docker labels  
ARG BUILD_DATE  
ARG BRANCH  
LABEL com.joyent.build-date=$BUILD_DATE \  
com.joyent.branch=$BRANCH  
  
# On macOS, with SSH keys and a Triton config in expected places  
# docker run --rm -it -v ~/.ssh:/root/.ssh -v ~/.triton:/root/.triton triton-
sandbox bash  

