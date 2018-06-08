FROM alpine:3.6  
LABEL maintainer "L3msh0@gmail.com"  
  
ARG SKIPFISH_VERSION=2.10b  
  
RUN \  
apk add --upgrade --no-cache openssl perl pcre libidn ca-certificates && \  
update-ca-certificates && \  
apk add --upgrade --no-cache --virtual .build-tools libc-dev make gcc openssl-
dev pcre-dev libidn-dev && \  
wget "https://github.com/l3msh0/skipfish/archive/${SKIPFISH_VERSION}.tar.gz"
-O /tmp/skipfish.tar.gz && \  
adduser -D -h /skipfish skipfish && \  
tar zxf /tmp/skipfish.tar.gz --strip-components=1 -C /skipfish && \  
rm /tmp/skipfish.tar.gz && \  
cd /skipfish && \  
make && \  
chmod 755 /skipfish/skipfish && \  
chown -R skipfish:skipfish /skipfish && \  
apk del --purge .build-tools && \  
mkdir /work && \  
chown skipfish:skipfish /work  
  
USER skipfish  
WORKDIR /skipfish  
  
VOLUME /work  
ENTRYPOINT ["./skipfish"]  
CMD ["-h"]

