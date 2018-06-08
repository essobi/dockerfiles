FROM travix/gocd-agent-gcloud:16.2.1  
  
MAINTAINER SignAlive  
  
# install packages  
RUN (curl --silent --location https://deb.nodesource.com/setup_4.x | bash -) \  
&& apt-get update \  
&& apt-get install -y \  
aufs-tools \  
build-essential \  
nodejs \  
parallel \  
git \  
redis-tools \  
&& apt-get clean \  
&& curl https://storage.googleapis.com/kubernetes-
release/release/v1.1.2/bin/linux/amd64/kubectl -o /usr/bin/kubectl \  
&& chmod +x /usr/bin/kubectl \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& npm install -g npm@^2.14.11 \  
&& npm install -g npm-cache@latest bower gulp grunt-cli  

