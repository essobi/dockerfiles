FROM timonier/node:latest  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
NPM_PROXY_CACHE_VERSION=latest  
  
RUN set -ex \  
\  
# Install runk/npm-proxy-cache  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/runk/npm-proxy-cache/${NPM_PROXY_CACHE_VERSION}" | xargs)
\  
&& npm install -g \  
"npm-proxy-cache@${NPM_PROXY_CACHE_VERSION}"  

