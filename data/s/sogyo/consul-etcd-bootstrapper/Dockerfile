FROM sogyo/consul:latest  
  
MAINTAINER Kevin van der Vlist <kvdvlist@sogyo.nl>  
  
RUN apk update \  
&& apk add wget go git gcc musl-dev \  
&& GOPATH=/go go get github.com/kevinvandervlist/consul-etcd-bootstrapper \  
&& cd /bin \  
&& GOPATH=/go go build github.com/kevinvandervlist/consul-etcd-bootstrapper \  
&& rm -rf /go \  
&& apk del wget go git gcc musl-dev \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT [ "/bin/consul-etcd-bootstrapper" ]  
  
CMD []

