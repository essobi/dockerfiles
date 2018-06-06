FROM atlassian/bamboo-base-agent  
MAINTAINER Ben Youngblood <ben.youngblood@colonyamerican.com>  
  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 4.1.2  
RUN apt-get update && apt-get install -y curl make git  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc  
  
RUN npm -g install npm@3.x  
  
RUN apt-get install wget  
  
RUN wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh  
  
RUN apt-get install -y python \  
&& curl -O https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& pip install awscli  
  
RUN wget https://storage.googleapis.com/golang/go1.5.1.linux-amd64.tar.gz \  
&& tar -C /usr/local -xzf go1.5.1.linux-amd64.tar.gz  
  
ENV PATH $PATH:/usr/local/go/bin  
  
ADD bamboo-capabilities.properties /root/bamboo-agent-home/bin/bamboo-
capabilities.properties  

