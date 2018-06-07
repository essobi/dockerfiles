FROM alpine:3.6  
MAINTAINER Jeremy Wells <jemmyw@gmail.com>  
  
  
RUN mkdir -p /opt/go/bin; mkdir -p /opt/go/src  
ENV GOPATH /opt/go  
ENV GOBIN /opt/go/bin  
ENV PATH $GOBIN:$PATH  
RUN apk update && apk upgrade && apk add zip ca-certificates curl git go make
musl-dev libc-dev g++ bash fakeroot \  
&& go get -u github.com/hashicorp/terraform \  
&& cd /opt/go/src/github.com/hashicorp/terraform \  
&& XC_OS=linux XC_ARCH=amd64 make bin \  
&& go get -u github.com/terraform-providers/terraform-provider-logentries \  
&& go get -u github.com/terraform-providers/terraform-provider-null \  
&& go get -u github.com/terraform-providers/terraform-provider-aws \  
&& go get -u github.com/terraform-providers/terraform-provider-template \  
&& cd /opt/go/src/github.com/terraform-providers \  
&& for m in `ls`; do echo $m; cd $m && make build && cd ..; done \  
&& rm -rf /opt/go/src \  
&& apk del git make musl-dev libc-dev g++ fakeroot  
  
RUN terraform -version  
RUN mkdir /app  
WORKDIR /app  
ENTRYPOINT ["$GOBIN/terraform"]  

