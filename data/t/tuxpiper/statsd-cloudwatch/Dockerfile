FROM node:6.12-alpine  
  
ENV STATSD_VERSION 0.8.0  
RUN apk add --no-cache curl python make g++ && \  
curl -L https://github.com/etsy/statsd/archive/v${STATSD_VERSION}.tar.gz | tar
-C /opt -xz -f - && \  
ln -s /opt/statsd-${STATSD_VERSION} /opt/statsd && \  
cd /opt/statsd && \  
npm install && \  
npm install https://github.com/camitz/aws-cloudwatch-statsd-
backend/archive/466e70135e108e6de3b7b421bf446c2b5c90be64.tar.gz && \  
curl -sL
https://github.com/jwilder/dockerize/releases/download/v0.5.0/dockerize-linux-
amd64-v0.5.0.tar.gz | tar zxf - -C /bin/ && \  
apk del --no-cache make g++  
  
WORKDIR /opt/statsd  
  
ADD config.js.tmpl .  
  
ENTRYPOINT [ "/bin/dockerize", "-template", "config.js.tmpl:config.js" ]  
CMD [ "./bin/statsd", "config.js" ]  

