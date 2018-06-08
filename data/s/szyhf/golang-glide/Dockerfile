FROM szyhf/alpine-glibc  
  
LABEL MAINTAINER="Back Yu <yhfszb@gamil.com>"  
  
# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g'
/etc/apk/repositories  
  
ENV GO_VERSION=1.10  
ENV GO_OS=linux-amd64  
ENV GOPATH=/root/go  
ENV PATH=$PATH:$GOPATH/bin:/usr/local/go/bin  
ENV GLIDE_HOME=/root/.glide  
  
RUN apk update \  
&& apk --no-cache add wget ca-certificates curl git openssh gcc musl-dev \  
&& wget --quiet
https://storage.googleapis.com/golang/go${GO_VERSION}.${GO_OS}.tar.gz \  
&& mkdir -p /usr/local/go \  
&& tar -C /usr/local -xzf go${GO_VERSION}.${GO_OS}.tar.gz \  
&& rm -rf go${GO_VERSION}.${GO_OS}.tar.gz \  
&& mkdir -p /root/go/src /root/go/bin /root/go/pkg /root/.glide \  
&& go get -v github.com/Masterminds/glide

