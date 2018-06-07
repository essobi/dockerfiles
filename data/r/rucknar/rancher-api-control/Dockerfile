#Rancher API control script Dockerfile  
FROM alpine  
MAINTAINER Ed Marshall (ed.marshall@infinityworks.com)  
  
ENV RUN=false  
  
RUN apk --update add curl  
  
# Install compile and install confd  
ENV CONFD_VERSION=v0.11.0 GOMAXPROCS=2 \  
GOROOT=/usr/lib/go \  
GOPATH=/opt/src \  
GOBIN=/gopath/bin  
  
RUN apk add --update go git gcc musl-dev \  
&& mkdir -p /opt/src; cd /opt/src \  
&& git clone -b "$CONFD_VERSION" https://github.com/kelseyhightower/confd.git
\  
&& cd $GOPATH/confd/src/github.com/kelseyhightower/confd \  
&& GOPATH=$GOPATH/confd/vendor:$GOPATH/confd CGO_ENABLED=0 go build -v
-installsuffix cgo -ldflags '-extld ld -extldflags -static' -a -x . \  
&& mv ./confd /usr/bin/ \  
&& chmod +x /usr/bin/confd \  
&& apk del go git gcc musl-dev \  
&& rm -rf /var/cache/apk/* /opt/src \  
&& mkdir -p /etc/confd/templates /etc/confd/conf.d  
  
COPY confd/tmpl/* /etc/confd/templates/  
COPY confd/toml/* /etc/confd/conf.d/  
COPY *.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/run.sh  
  
CMD /usr/local/bin/run.sh  

