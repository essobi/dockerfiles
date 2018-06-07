FROM alpine:3.6  
MAINTAINER Ohze JSC <thanhbv@sandinh.net>  
  
ARG VERSION_TAG=v1.0.0  
ENV MD_ENDPOINT=lb.minio:9000/ \  
MD_KEY=minio \  
MD_SECRET=minio123 \  
MD_HTTPS=true \  
MD_BUCKET_NAME=xenforo \  
MD_PORT=":9004"  
RUN \  
apk add --no-cache ca-certificates && \  
apk add --no-cache --virtual .build-deps curl && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
curl -L https://github.com/ohze/minio-delayed-
server/releases/download/$VERSION_TAG/minio-delayed-server \  
> /usr/bin/minio-delayed-server && \  
chmod +x /usr/bin/minio-delayed-server && \  
apk del .build-deps  
  
EXPOSE $MD_PORT  
  
CMD ["minio-delayed-server"]  

