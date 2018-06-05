FROM ubuntu:16.04  
MAINTAINER Bohdan Kolecek <kolecek@apollo13.cz>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
# Setting TERM to flawlessly run console applications like mc, nano when
connecting interactively via docker exec  
TERM=xterm  
  
# Install:  
# 1. GIT for accessing repositories  
# 2. MC and telnet just for convenience  
# 3. redis-cli for obtaining configuration  
# 4. python2, curl for installing AWS cli  
# 6. nc for wait-for-service.sh script  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
git \  
mc \  
redis-tools \  
curl \  
python \  
netcat-openbsd \  
telnet && \  
# Install AWS CLI  
curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
rm -rf ./awscli-bundle && \  
rm ./awscli-bundle.zip && \  
# Clean up  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add client for configuration service, entrypoint for initializing
environment variables with container configuration, etc.  
COPY config-service/* bin/build.sh bin/git-pull.sh bin/update.sh bin/load-
config.sh bin/service-reload.sh bin/config-watcher.sh bin/wait-for-service.sh
/usr/local/bin/  
  
COPY bin/env.sh /  
  
ENTRYPOINT [ "/env.sh" ]  

