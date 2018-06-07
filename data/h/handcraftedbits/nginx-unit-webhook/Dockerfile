FROM handcraftedbits/nginx-unit:1.1.3  
MAINTAINER HandcraftedBits <opensource@handcraftedbits.com>  
  
ARG WEBHOOK_VERSION=2.6.5  
  
COPY data /  
  
RUN apk update update && \  
apk add git go libc-dev && \  
  
mkdir -p /opt/webhook && \  
mkdir -p /opt/gopath/src/github.com/adnanh && \  
cd /opt/gopath/src/github.com/adnanh && \  
git clone https://github.com/adnanh/webhook && \  
cd webhook && \  
git checkout tags/${WEBHOOK_VERSION} && \  
export GOPATH=/opt/gopath && \  
git config --global http.https://gopkg.in.followRedirects true && \  
  
go get github.com/codegangsta/negroni && \  
go get github.com/ghodss/yaml && \  
go get github.com/gorilla/mux && \  
go get gopkg.in/fsnotify.v1 && \  
  
go install ./... && \  
mv /opt/gopath/bin/webhook /opt/webhook/webhook && \  
cd /opt && \  
rm -rf gopath && \  
  
apk del git go libc-dev  
  
EXPOSE 9000  
  
CMD [ "/bin/bash", "/opt/container/script/run-webhook.sh" ]  

