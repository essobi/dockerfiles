FROM alpine  
MAINTAINER toor-t  
  
RUN apk --no-cache add nodejs && \  
npm -g --no-progress --registry http://registry.npmjs.org/ install cordova &&
\  
npm cache clean && \  
cordova telemetry off  
  
VOLUME /work  
WORKDIR /work  

