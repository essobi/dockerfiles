FROM node:8-alpine  
RUN apk add --update \  
openssh \  
curl \  
wget \  
ca-certificates \  
tar \  
unzip \  
python \  
python-dev \  
py-pip \  
build-base \  
&& pip install virtualenv \  
&& rm -rf /var/cache/apk/* \  
&& update-ca-certificates  
RUN curl https://s3.amazonaws.com/aws-cli/awscli-bundle.zip \  
-o awscli-bundle.zip && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
rm awscli-bundle.zip && rm -rf awscli-bundle  
RUN npm install -g pm2  

