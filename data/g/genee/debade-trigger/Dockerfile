FROM alpine:3.4  
ADD . /app  
RUN apk add --no-cache nodejs libzmq python make g++ zeromq-dev && cd /app &&
npm install \  
&& mkdir -p /etc/debade && cp config/debade.sample.yml /etc/debade/trigger.yml
\  
&& apk del zeromq-dev g++ make python  
  
WORKDIR /app  
CMD ["/usr/bin/node", "/app/index.js", "-c", "/etc/debade/trigger.yml"]

