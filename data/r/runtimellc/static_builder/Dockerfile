FROM ubuntu:16.04  
  
MAINTAINER RuntimeLLC  
LABEL version="0.1"  
  
ENV NODE_VERSION="6"  
ENV DEPENDENCIES="curl build-essential ca-certificates"  
#Install dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends ${DEPENDENCIES} \  
&& rm -rf /var/lib/apt/lists/*  
#Install and configure git  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends git \  
&& rm -rf /var/lib/apt/lists/* \  
&& git config --global url."https://github".insteadOf git://github  
  
#Install node-js  
RUN curl -sL https://deb.nodesource.com/setup_${NODE_VERSION}.x | bash - \  
&& apt-get install -y --no-install-recommends nodejs \  
&& npm set progress=false \  
&& rm -rf /var/lib/apt/lists/*  
#Install and configure bower  
RUN npm install -g bower \  
&& echo '{"allow_root": true}' > ~/.bowerrc  

