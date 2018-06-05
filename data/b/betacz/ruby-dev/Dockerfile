FROM betacz/ruby:1.9.3  
MAINTAINER Beta CZ <hlj8080@gmail.com>  
  
ENV HOME /root  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# node 0.12.0  
RUN apt-get update && apt-get install -y \  
ca-certificates  
  
ENV NODE_VERSION 0.12.0  
ENV NPM_VERSION 2.5.1  
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
  
RUN npm install -g cnpm --registry=https://registry.npm.taobao.org \  
&& npm cache clean  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

