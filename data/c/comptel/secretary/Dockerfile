FROM alpine:3.4  
ENV DUMB_INIT_VERSION 1.1.3  
ENV SECRETARY_VERSION fwd-master  
  
RUN addgroup secretary && \  
adduser -S -G secretary secretary  
  
COPY docker-entrypoint.sh /  
COPY secretary-Linux-x86_64 /usr/bin/secretary  
  
# Set up certificates, base tools, dumb-init and secretary.  
RUN apk add --no-cache ca-certificates openssl curl bash && \  
wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 && \  
chmod +x /usr/bin/secretary /usr/bin/dumb-init && \  
mkdir -p /secretary/keys && \  
chmod 0700 /secretary/keys && \  
chown secretary:secretary /docker-entrypoint.sh && \  
chown -R secretary:secretary /secretary && \  
apk del openssl && \  
rm -rf /var/cache/apk/*  
  
USER secretary  
  
WORKDIR /secretary  
  
EXPOSE 5070  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["secretary", "daemon"]  

