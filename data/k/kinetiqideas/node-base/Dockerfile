# https://hub.docker.com/_/node/  
FROM node:6.11.5  
# Install dependencies  
RUN apt-get update -q \  
&& apt-get install -yqq \  
curl \  
python-dev \  
unzip \  
git \  
ssh \  
gcc \  
make \  
build-essential \  
libkrb5-dev \  
sudo \  
apt-utils \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install the AWS CLI  
RUN cd /tmp && curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" \  
-o "awscli-bundle.zip" && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
rm awscli-bundle.zip && rm -rf awscli-bundle  
  
# Protip 4: Add a Process ID Safety Net  
# https://nodesource.com/blog/8-protips-to-start-killing-it-when-dockerizing-
node-js/  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.1.1/dumb-
init_1.1.1_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init

