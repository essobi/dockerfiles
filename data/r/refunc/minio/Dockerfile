# Stage build  
FROM golang:1.10-alpine3.7 as BUILDER  
  
ENV GOPATH /go  
ENV PATH $PATH:$GOPATH/bin  
ENV CGO_ENABLED 0  
ENV MINIO_RELEASE refunc  
  
RUN \  
apk add --no-cache --virtual .build-deps git && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf  
  
ENV MINIO_VERSION="RELEASE.2018-04-04T05-20-54Z-refunc-1"  
RUN \  
mkdir -p /go/src/github.com/minio && \  
git clone https://github.com/antmanler/minio.git
/go/src/github.com/minio/minio && \  
cd /go/src/github.com/minio/minio && \  
git checkout ${MINIO_VERSION}  
  
COPY . /go/src/github.com/minio/minio/refunc  
  
RUN \  
cd /go/src/github.com/minio/minio/refunc && \  
go install -v -ldflags "$(go run ../buildscripts/gen-ldflags.go)"  
  
# Stage release  
FROM alpine:3.7  
LABEL maintainer="antmanler(wo@zhaob.in)"  
  
COPY dockerscripts/docker-entrypoint.sh dockerscripts/healthcheck.sh /usr/bin/  
  
ENV MINIO_UPDATE off  
  
RUN \  
apk add --no-cache ca-certificates curl && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
chmod +x /usr/bin/docker-entrypoint.sh && \  
chmod +x /usr/bin/healthcheck.sh  
  
EXPOSE 9000  
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]  
  
VOLUME ["/export"]  
  
HEALTHCHECK \--interval=30s --timeout=5s \  
CMD /usr/bin/healthcheck.sh  
  
COPY \--from=builder /go/bin/refunc /usr/bin/minio  
  
CMD ["minio"]  

