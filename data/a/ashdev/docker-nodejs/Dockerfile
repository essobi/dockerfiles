FROM debian:wheezy  
MAINTAINER AshDev <ashdevfr@gmail.com>  
  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
python build-essential git ca-certificates  
RUN mkdir /nodejs && curl
https://nodejs.org/dist/v4.2.6/node-v4.2.6-linux-x64.tar.gz | tar xvzf - -C
/nodejs --strip-components=1  
  
ENV PATH $PATH:/nodejs/bin  

