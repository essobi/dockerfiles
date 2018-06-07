FROM webhippie/alpine:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
VOLUME ["/var/lib/drone"]  
  
EXPOSE 8000  
WORKDIR /root  
CMD ["/bin/s6-svscan", "/etc/s6"]  
  
ENV DRONE_PATH github.com/drone/drone  
ENV DRONE_REPO https://${DRONE_PATH}.git  
ENV DRONE_BRANCH master  
  
ENV GOPATH /usr/local  
  
RUN apk update && \  
mkdir -p \  
/var/lib/drone && \  
apk add \  
build-base \  
go \  
git && \  
go get -u \  
github.com/jteeuwen/go-bindata/... && \  
go get -u \  
github.com/elazarl/go-bindata-assetfs/... && \  
go get -u \  
github.com/drone/mq/... && \  
go get -u \  
github.com/tidwall/redlog && \  
go get -u \  
github.com/drone/drone-ui/dist && \  
git clone \  
-b ${DRONE_BRANCH} \  
${DRONE_REPO} \  
/usr/local/src/${DRONE_PATH} && \  
cd \  
/usr/local/src/${DRONE_PATH} && \  
go generate -v \  
${DRONE_PATH}/server/template && \  
go generate -v \  
${DRONE_PATH}/store/datastore/ddl && \  
go install \  
${DRONE_PATH}/drone && \  
cp -f \  
/usr/local/bin/drone \  
/usr/bin/ && \  
apk del \  
build-base \  
go \  
git && \  
rm -rf \  
/var/cache/apk/* \  
/usr/local/*  
  
ADD rootfs /  

