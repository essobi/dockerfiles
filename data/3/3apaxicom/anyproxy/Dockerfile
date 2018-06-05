FROM node:4.0.0  
MAINTAINER docker-anyproxy@3apaxi.com  
ENV ANYPROXY_VERSION=3.8.0  
EXPOSE 8001  
EXPOSE 8002  
EXPOSE 8003  
EXPOSE 8088  
RUN echo "#!/bin/sh" > /usr/bin/open && \  
echo "exit 0" >> /usr/bin/open &&\  
chmod +x /usr/bin/open  
  
RUN npm install --no-optional --only=production --quiet --global --no-color
anyproxy@$ANYPROXY_VERSION  
  
ENV HOME /anyproxy  
RUN mkdir /anyproxy  
RUN anyproxy -g  
WORKDIR /anyproxy  
VOLUME /anyproxy  
  
CMD ["anyproxy", "--intercept"]  

