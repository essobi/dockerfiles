FROM buildpack-deps:jessie  
  
MAINTAINER Percy Zhang <mr.zhangping@gmail.com>  
  
RUN apt-get update && apt-get install -y wget  
RUN wget http://nodejs.org/dist/v0.12.0/node-v0.12.0-linux-x64.tar.gz  
RUN tar -xzf "node-v0.12.0-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v0.12.0-linux-x64.tar.gz" \  
&& npm install -g npm@2.5.0 \  
&& npm cache clear  
  
CMD "node"  
  

