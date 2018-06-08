FROM debian:wheezy  
  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
xz-utils python build-essential git ca-certificates  
RUN mkdir /nodejs && curl
https://nodejs.org/dist/v4.4.4/node-v4.4.4-linux-x64.tar.xz | tar xvJf - -C
/nodejs --strip-components=1  
  
ENV PATH $PATH:/nodejs/bin  

