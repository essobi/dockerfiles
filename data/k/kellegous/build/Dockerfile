FROM ubuntu:xenial  
  
RUN apt-get update \  
&& apt-get install -y \  
golang \  
git \  
ruby \  
ruby-dev \  
nodejs \  
npm \  
build-essential \  
closure-compiler \  
curl \  
protobuf-compiler \  
&& ln -s /usr/bin/nodejs /usr/bin/node \  
&& npm install -g typescript \  
&& gem install rake sass \  
&& apt-get clean  

