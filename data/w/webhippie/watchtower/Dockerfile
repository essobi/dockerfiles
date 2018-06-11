FROM webhippie/alpine:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
WORKDIR /root  
CMD ["/bin/s6-svscan", "/etc/s6"]  
  
ENV WATCHTOWER_PATH github.com/v2tec/watchtower  
ENV WATCHTOWER_REPO https://${WATCHTOWER_PATH}.git  
ENV WATCHTOWER_BRANCH master  
  
ENV GOPATH /usr/local  
  
RUN apk add --no-cache --virtual build-dependencies build-base go git && \  
go get -u github.com/Masterminds/glide && \  
git clone -b ${WATCHTOWER_BRANCH} ${WATCHTOWER_REPO}
/usr/local/src/${WATCHTOWER_PATH} && \  
cd /usr/local/src/${WATCHTOWER_PATH} && \  
glide install --skip-test && \  
go install ${WATCHTOWER_PATH} && \  
cp /usr/local/bin/watchtower /usr/bin/ && \  
apk del build-dependencies && \  
rm -rf /usr/local/*  
  
ADD rootfs /  

