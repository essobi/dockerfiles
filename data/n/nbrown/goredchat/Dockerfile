FROM alpine  
MAINTAINER Nigel Brown <nigel@windsock.io>  
  
ENV PATH /go/bin:/usr/local/go/bin:$PATH  
ENV GOPATH /go  
  
COPY . /go/src/github.com/nbrownuk/goredchat  
  
RUN set -x && \  
apk update && \  
apk add go git && \  
cd /go/src/github.com/nbrownuk/goredchat && \  
go get -d -v github.com/nbrownuk/goredchat && \  
go build -a -tags netgo -installsuffix netgo -ldflags -w -o /goredchat . && \  
apk del go git && \  
rm -rf /var/cache/apk/* && \  
rm -rf /go  
  
CMD ["--help"]  
  
ENTRYPOINT ["/goredchat"]  

