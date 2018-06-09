FROM mhart/alpine-node:5  
MAINTAINER Vincent Demeester <vincent@sbr.pm>  
  
ENV STACKEDIT_VERSION 3.1.14  
RUN apk add --no-cache curl && \  
curl -o v${STACKEDIT_VERSION}.tar.gz -sSL
https://github.com/benweet/stackedit/archive/v${STACKEDIT_VERSION}.tar.gz && \  
tar -xzf v${STACKEDIT_VERSION}.tar.gz && \  
rm v${STACKEDIT_VERSION}.tar.gz && \  
mv stackedit-${STACKEDIT_VERSION} stackedit && \  
cd stackedit && \  
npm install && \  
apk del curl  
  
WORKDIR /stackedit  
  
EXPOSE 3000  
CMD node server.js  
  

