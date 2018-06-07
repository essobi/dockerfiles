FROM java:alpine  
MAINTAINER ShiYi <me@shiyicode.com>  
  
RUN apk upgrade --update; \  
apk add linux-headers; \  
apk add libc-dev; \  
apk add bash; \  
apk add git; \  
apk add curl; \  
apk add python; \  
apk add g++; \  
apk add gcc; \  
curl https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz | tar xzf
- -C /; \  
mv /go /goroot; \  
mkdir /lib64; \  
ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2;  
  
ENV GOPATH /go  
ENV GOROOT /goroot  
ENV GOBIN=$GOPATH/bin  
ENV PATH=$PATH:$GOROOT/bin  
  
RUN mkdir -p /go/src;  
  
ADD ./ /go/src/oj-judger  
  
RUN cd /go/src/oj-judger; \  
./build.sh; \  
cd output;  
  
WORKDIR /go/src/oj-judger/output  
  
CMD ./oj-judger -c cfg/cfg.toml.release

