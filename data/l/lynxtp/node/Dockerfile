FROM lynxtp/ubuntu:15.10  
MAINTAINER "Tom Vaughan <tvaughan@lynxtp.com>"  
  
ENV PATH /opt/node/bin:$PATH  
  
RUN curl -sL -o /tmp/node.tar.gz
https://nodejs.org/dist/v5.9.0/node-v5.9.0-linux-x64.tar.gz \  
&& mkdir -p /opt/node \  
&& tar \--strip-components=1 -C /opt/node -xf /tmp/node.tar.gz \  
&& rm -f /tmp/node.tar.gz  
  
# https://www.npmjs.com/package/npm-check-updates  
RUN npm install -g npm-check-updates  
  
CMD ["node"]  

