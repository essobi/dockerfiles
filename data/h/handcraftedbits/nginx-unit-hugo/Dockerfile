FROM handcraftedbits/nginx-unit-webhook:2.6.5  
MAINTAINER HandcraftedBits <opensource@handcraftedbits.com>  
  
ARG HUGO_VERSION=v0.30.2  
  
COPY data /  
  
ENV GOPATH /opt/gopath/  
RUN apk update && \  
  
apk add git go libc-dev && \  
go get -u -d github.com/magefile/mage && \  
cd /opt/gopath/src/github.com/magefile/mage && \  
go run bootstrap.go && \  
mkdir -p /opt/hugo && \  
mkdir -p /opt/gopath/src/github.com/gohugoio && \  
cd /opt/gopath/src/github.com/gohugoio && \  
git clone https://github.com/gohugoio/hugo && \  
cd hugo && \  
git checkout tags/${HUGO_VERSION} && \  
export GOPATH=/opt/gopath && \  
export PATH=$PATH:$GOPATH/bin && \  
mage hugo && \  
mv hugo /opt/hugo/hugo && \  
cd /opt && \  
rm -rf gopath && \  
  
apk del go libc-dev  
  
CMD [ "/bin/bash", "/opt/container/script/run-hugo.sh" ]  

