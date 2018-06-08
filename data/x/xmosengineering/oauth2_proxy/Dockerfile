FROM ubuntu:14.04  
MAINTAINER David Lacey <davel@xmos.com>  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
RUN apt-get update && apt-get install -y golang gcc git curl tar gzip  
ADD download.sh download.sh  
RUN ./download.sh bitly oauth2_proxy 7ba51ba9f23fc7412864d1  
RUN mkdir /go  
ENV GOPATH /go  
ENV GOBIN /bin  
ADD providers.go oauth2_proxy/providers/providers.go  
ADD phabricator.go oauth2_proxy/providers/phabricator.go  
RUN mkdir -p /go/src/github.com/bitly && \  
mv oauth2_proxy /go/src/github.com/bitly && \  
go get github.com/bitly/oauth2_proxy  
ADD run_proxy.sh run_proxy.sh  
ENTRYPOINT ["./run_proxy.sh"]  

