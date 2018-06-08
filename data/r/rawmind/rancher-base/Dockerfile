FROM docker.io/alpine:3.3  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
# Install basic packages and config monit  
RUN apk add --update bash monit openssl openssh curl && rm -rf
/var/cacke/apk/* \  
&& mkdir -p /etc/monit/conf.d/  
COPY monit/monitrc /etc/monitrc  
RUN chown root:root /etc/monitrc && chmod 700 /etc/monitrc  
COPY monit/basic /etc/monit/conf.d/basic  
  
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
  
# Install selfsigned ca (optional)  
#COPY <ca.crt> /etc/ssl/certs/<ca.pem>  
#RUN cat /etc/ssl/certs/<ca.pem> >> /etc/ssl/certs/ca-certificates.crt && \  
#cd /etc/ssl/certs/ && \  
#ln -s <ca.pem> `openssl x509 -hash -noout -in <ca.pem>`.0  
CMD ["/usr/bin/monit", "-I"]  

