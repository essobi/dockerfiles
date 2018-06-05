FROM node:6.9.2  
MAINTAINER 411164348@qq.com  
ENV ANYPROXY_VERSION=3.10.3  
EXPOSE 8001  
EXPOSE 8002  
RUN echo "#!/bin/sh" > /usr/bin/open && \  
echo "exit 0" >> /usr/bin/open &&\  
chmod +x /usr/bin/open  
  
RUN npm install --global anyproxy@$ANYPROXY_VERSION  
  
ENV HOME /anyproxy  
RUN mkdir /anyproxy  
RUN anyproxy -g  
WORKDIR /anyproxy  
VOLUME /anyproxy  
  
RUN anyproxy --intercept --file /anyproxy/anyproxy.log  

