FROM webhippie/alpine:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
ENV SHERDOCK_PATH github.com/rancher/sherdock  
ENV SHERDOCK_REPO https://${SHERDOCK_PATH}.git  
ENV SHERDOCK_BRANCH master  
  
ENV GOPATH /usr:/usr/src/${SHERDOCK_PATH}/Godeps/_workspace  
  
RUN apk update && \  
apk add \  
build-base \  
go \  
git && \  
git clone -b ${SHERDOCK_BRANCH} ${SHERDOCK_REPO} /usr/src/${SHERDOCK_PATH} &&
\  
cd /usr/src/${SHERDOCK_PATH} && \  
go get -u github.com/tools/godep && \  
godep go install ${SHERDOCK_PATH} && \  
apk del build-base go git && \  
rm -rf /var/cache/apk/* && \  
rm -r \  
/usr/src/* \  
/usr/pkg/* \  
/usr/bin/godep  
  
ADD rootfs /  
EXPOSE 8080  
WORKDIR /root  
CMD ["/bin/s6-svscan", "/etc/s6"]  

