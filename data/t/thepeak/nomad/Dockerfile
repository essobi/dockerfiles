FROM alpine:3.7  
  
RUN apk update \  
&& apk add -t build go make musl-dev bash git \  
&& apk add ca-certificates \  
&& wget https://github.com/hashicorp/nomad/archive/v0.8.1.tar.gz -O
/tmp/nomad.tar.gz \  
&& mkdir -p /go/src/github.com/hashicorp/nomad/ \  
&& tar xvf /tmp/nomad.tar.gz --strip-components 1 -C
/go/src/github.com/hashicorp/nomad/ \  
&& cd /go/src/github.com/hashicorp/nomad/ \  
&& GOPATH=/go make GO_TAGS=ui pkg/linux_amd64/nomad \  
&& mv /go/src/github.com/hashicorp/nomad/pkg/linux_amd64/nomad /usr/bin/ \  
&& rm -rf /go \  
&& rm -rf /tmp/nomad.tar.gz \  
&& apk del build  
  
ENTRYPOINT ["nomad"]  

