FROM ubuntu:16.04  
ENV PORT=80  
RUN apt-get update  
RUN apt-get install -y --force-yes nodejs nodejs-legacy npm git openssh-client  
  
RUN mkdir -p /root/git-proxy  
COPY package.json /root/git-proxy/package.json  
  
WORKDIR /root/git-proxy  
RUN bash -c 'npm update || echo'  
COPY . /root/git-proxy  
  
CMD node server.js

