FROM travix/gocd-agent-gcloud:18.5.0  
  
MAINTAINER Travix  
  
# install packages  
RUN (curl --silent --location https://deb.nodesource.com/setup_8.x | bash -) \  
&& apt-get update \  
&& apt-get install -y \  
aufs-tools \  
build-essential \  
nodejs \  
parallel \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& npm install -g npm@next \  
&& npm install -g npm-cache@latest  

