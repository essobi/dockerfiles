FROM thenativeweb/wolkenkit-box-node:1.2.0  
MAINTAINER the native web <hello@thenativeweb.io>  
  
RUN mkdir -p /wolkenkit/app  
CMD [ "/bin/sh" ]  
  
ONBUILD ADD ./package.json /wolkenkit/app/package.json  
ONBUILD RUN cd /wolkenkit/app && \  
npm install --production --silent  

