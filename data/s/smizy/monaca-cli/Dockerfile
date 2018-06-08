FROM pottava/nodejs  
MAINTAINER smizy  
  
RUN adduser -D -g '' -u 1000 docker  
  
RUN apk --no-cache add git && \  
npm install -g cordova@6.0 monaca && \  
mkdir /app  
  
USER docker  
WORKDIR /app  
  
VOLUME ["/opt/node/lib/node_modules"]  
  
CMD ["sh"]  

