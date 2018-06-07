FROM alpine:3.5  
ENV \  
TIMEZONE=Europe/Kiev  
  
RUN \  
# Add edge repo  
echo '@edge http://dl-cdn.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories && \  
echo '@edge http://dl-cdn.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories && \  
echo '@edge http://dl-cdn.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
  
# Update packages  
apk --no-cache upgrade && \  
  
# Install Bash  
apk --no-cache add bash && \  
  
# Install SSL  
# Alpine 3.5 switched from OpenSSL to LibreSSL  
apk --no-cache add libressl && \  
  
# Set timezone  
apk --no-cache add tzdata && \  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone && \  
apk del tzdata  
  
ENTRYPOINT ["bash"]  

