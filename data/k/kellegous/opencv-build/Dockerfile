FROM kellegous/opencv  
  
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
&& curl -OL
https://github.com/google/protobuf/releases/download/v3.1.0/protoc-3.1.0-linux-x86_64.zip
\  
&& unzip protoc-3.1.0-linux-x86_64.zip -d /usr/local \  
&& rm protoc-3.1.0-linux-x86_64.zip \  
&& ln -s /usr/bin/nodejs /usr/bin/node \  
&& npm install -g typescript \  
&& gem install rake sass \  
&& apt-get clean  

