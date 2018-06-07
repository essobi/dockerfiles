FROM alpine:3.7  
RUN \  
adduser -h /sass -s /sbin/nologin -D sass && \  
apk add --no-cache \  
dumb-init \  
libsass \  
sassc && \  
rm -f /tmp/* /etc/apk/cache/*  
  
RUN apk add --no-cache nodejs && \  
npm install node-sass  
  
WORKDIR /sass/assets  
VOLUME /sass/assets  
ENTRYPOINT [ "/node_modules/node-sass/bin/node-sass" ]  
CMD [ "--help" ]  

