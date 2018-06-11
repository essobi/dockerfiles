FROM yellowblackandwhite/alpine-base  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
USER root  
  
ENV GOROOT /usr/lib/go  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:$GOROOT/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH" && \  
apk --update add curl git mercurial bzr go gcc build-base && \  
apk del gcc build-base && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
  
COPY go-wrapper $GOPATH/bin/  
WORKDIR $GOPATH  
USER alpine  

