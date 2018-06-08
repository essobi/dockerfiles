FROM alpine:edge  
  
RUN apk update && \  
apk upgrade && \  
apk add --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/
--allow-untrusted tor && \  
apk add socat  
  
COPY torrc /tmp/torrc

