FROM debian  
  
MAINTAINER Mitsuru Kariya  
  
ENV HUGO_VERSION=0.39 NODE_VERSION=8.9.0  
RUN apt-get update && \  
apt-get install -y python-pygments curl xz-utils ssh rsync && \  
curl -sSL
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
| \  
tar xvfz - -C /usr/local/bin hugo && \  
curl -sSL
https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz
| \  
tar xvfJ - -C /usr/local \--strip-components=1 && \  
npm -g update && \  
npm -g install npm  

