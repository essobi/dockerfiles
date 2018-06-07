FROM alpine:3.5  
ENV \  
TZ=Europe/Kiev \  
TERM=xterm  
  
RUN \  
# Add edge repos  
echo '@edge http://dl-cdn.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories && \  
echo '@edge http://dl-cdn.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories && \  
echo '@edge http://dl-cdn.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
  
# Update packages  
apk update && \  
apk upgrade && \  
  
# Install Bash  
apk add bash && \  
  
# Install SSL  
# Alpine 3.5 switched from OpenSSL to LibreSSL  
apk add libressl ca-certificates && \  
  
# Install latest Timezone data  
apk add tzdata && \  
  
# Clean  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["bash"]  

