FROM alpine:latest  
MAINTAINER Maximilian Pachl <m@ximilian.info>  
  
# configuration and versions  
ENV BUILD_TOOLS="go git musl-dev"  
ENV GOPATH=/tmp/go  
  
ADD . /tmp/go/src/github.com/faryon93/sackci  
  
# compile and install sackci  
RUN cd /tmp/go/src/github.com/faryon93/sackci && \  
rm -rf /var/cache/apk/* && \  
apk add --no-cache $BUILD_TOOLS && \  
go get -v github.com/faryon93/sackci && \  
go build -v -ldflags "-X main.GIT_COMMIT=`git log --pretty=format:'%h' -n 1`"
\  
-o /tmp/go/bin/sackci \  
github.com/faryon93/sackci && \  
go get github.com/tianon/gosu && \  
cp /tmp/go/bin/sackci /usr/sbin/ && \  
cp /tmp/go/bin/gosu /usr/bin && \  
  
# remove build tools  
rm -rf /tmp/go && \  
apk del --purge $BUILD_TOOLS  
  
# entry script  
COPY entry.sh /  
RUN chmod +x /entry.sh  
  
RUN delgroup ping && \  
adduser -D -u 1000 -g 'sackci' sackci  
  
WORKDIR /sackci  
  
ENTRYPOINT ["/entry.sh"]

