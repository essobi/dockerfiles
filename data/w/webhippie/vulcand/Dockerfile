FROM webhippie/alpine:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
ENV VULCAND_PATH github.com/vulcand/vulcand  
ENV VULCAND_REPO https://${VULCAND_PATH}.git  
ENV VULCAND_BRANCH master  
  
ENV GOPATH /usr:/usr/src/${VULCAND_PATH}/Godeps/_workspace  
  
RUN apk update && \  
apk add \  
build-base \  
go \  
git && \  
git clone -b ${VULCAND_BRANCH} ${VULCAND_REPO} /usr/src/${VULCAND_PATH} && \  
cd /usr/src/${VULCAND_PATH} && \  
go get -u github.com/tools/godep && \  
godep go install ${VULCAND_PATH} && \  
godep go install ${VULCAND_PATH}/vctl && \  
godep go install ${VULCAND_PATH}/vbundle && \  
apk del build-base go git && \  
rm -rf /var/cache/apk/* && \  
rm -r \  
/usr/src/* \  
/usr/pkg/* \  
/usr/bin/godep  
  
ADD rootfs /  
EXPOSE 8181 8182  
WORKDIR /root  
CMD ["/bin/s6-svscan", "/etc/s6"]  

