FROM webhippie/alpine:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
VOLUME ["/var/lib/registry"]  
  
EXPOSE 5000  
WORKDIR /root  
CMD ["/bin/s6-svscan", "/etc/s6"]  
  
ENV REGISTRY_PATH github.com/docker/distribution  
ENV REGISTRY_REPO https://${REGISTRY_PATH}.git  
ENV REGISTRY_BRANCH master  
  
ENV GOPATH /usr/local  
  
RUN apk update && \  
mkdir -p \  
/var/lib/registry && \  
groupadd \  
-g 1000 \  
registry && \  
useradd \  
-u 1000 \  
-d /var/lib/registry \  
-g registry \  
-s /bin/bash \  
-M \  
registry && \  
apk add \  
build-base \  
go \  
git \  
mercurial \  
su-exec && \  
git clone -b ${REGISTRY_BRANCH} ${REGISTRY_REPO}
/usr/local/src/${REGISTRY_PATH} && \  
cd /usr/local/src/${REGISTRY_PATH} && \  
go install ${REGISTRY_PATH}... && \  
cp -f \  
/usr/local/bin/registry \  
/usr/local/bin/digest \  
/usr/local/bin/registry-api-descriptor-template \  
/usr/bin/ && \  
apk del \  
build-base \  
go \  
git \  
mercurial && \  
rm -rf \  
/var/cache/apk/* \  
/usr/local/*  
  
ADD rootfs /  

