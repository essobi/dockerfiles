FROM phusion/baseimage:latest  
  
CMD ["/sbin/my_init"]  
  
ENV CONFD_VERSION=v0.11.0 GOMAXPROCS=2 \  
GOROOT=/usr/lib/go \  
GOPATH=/opt/src \  
GOBIN=/gopath/bin  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y curl nginx git gcc musl-dev \  
&& mkdir -p /opt/src \  
&& cd /opt/src \  
&& curl -fL https://storage.googleapis.com/golang/go1.7.4.linux-amd64.tar.gz |
tar xzf - -C /usr/lib \  
&& cp /usr/lib/go/bin/go /bin/go \  
&& git clone -b "${CONFD_VERSION}"
https://github.com/kelseyhightower/confd.git \  
&& cd $GOPATH/confd/src/github.com/kelseyhightower/confd \  
&& GOPATH=$GOPATH/confd/vendor:$GOPATH/confd CGO_ENABLED=0 go build -v
-installsuffix cgo -ldflags '-extld ld -extldflags -static' -a -x . \  
&& mv ./confd /bin/ \  
&& chmod +x /bin/confd \  
&& apt-get remove -y git gcc musl-dev \  
&& rm -rf /opt/src \  
&& mkdir -p /etc/confd/templates /etc/confd/conf.d \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/nginx/sites-
enabled/default  
  
ADD confd/*.toml /etc/confd/conf.d/  
ADD confd/*.tmpl /etc/confd/templates/  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD default-site.conf /etc/nginx/sites-enabled/default.conf  
  
ADD start.sh /bin  
ADD run_nginx.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run /bin/start.sh  

