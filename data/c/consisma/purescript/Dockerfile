FROM node:0.10.36  
ENV DEBIAN_FRONTEND noninteractive  
  
MAINTAINER majbilou@consisma.com  
  
ENV PURESCRIPT_VERSION 0.6.8  
RUN apt-get update && apt-get install -y wget\  
&& npm update -g npm\  
&& npm install -g grunt-cli bower\  
&& mkdir /platform && cd /platform\  
&& wget
https://github.com/purescript/purescript/releases/download/v${PURESCRIPT_VERSION}/linux64.tar.gz\  
&& cd /platform && tar -xvf linux64.tar.gz\  
&& rm /platform/linux64.tar.gz  
  
ENV PATH /platform/purescript:$PATH  
  
WORKDIR /app  
  
CMD ["psci"]  

