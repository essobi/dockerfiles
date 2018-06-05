FROM php:7.2-cli-stretch  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && apt-get install -yqq --no-install-recommends \  
ca-certificates \  
git \  
wget \  
zip unzip \  
jq \  
patch \  
expect \  
tcl8.6 \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV DOCKER_VERSION 17.04.0-ce  
RUN curl -fsSL \  
"https://get.docker.com/builds/$(uname -s)/$(uname
-m)/docker-${DOCKER_VERSION}.tgz" | tar xz > docker \  
&& mv docker/docker /usr/local/bin/docker \  
&& rm -rf docker  
  
# Install composer.  
RUN php -r "readfile('https://getcomposer.org/installer');" | php && mv
composer.phar /usr/local/bin/composer  
  
# Install Rancher CLI  
ENV RANCHER_CLI_VERSION 0.6.8  
RUN curl -fsSL \  
"https://github.com/rancher/cli/releases/download/v${RANCHER_CLI_VERSION}/rancher-
linux-amd64-v${RANCHER_CLI_VERSION}.tar.gz" \  
| tar xz \  
&& mv rancher-v${RANCHER_CLI_VERSION}/rancher /usr/local/bin/rancher \  
&& rm -rf rancher-v${RANCHER_CLI_VERSION}  
  
COPY *.sh /  
  
RUN useradd -ms /bin/bash runner  
ENV HOME /home/runner  
VOLUME ["/builds"]  
  
ENTRYPOINT ["/bootstrap.sh"]  

