FROM alpine  
MAINTAINER Oluwaseun Obajobi <oba@obajobi.com>  
  
RUN apk add --update nginx openssl && rm -rf /var/cache/apk/*  
  
ENV CONFD_VERSION 0.9.0  
RUN wget -O /bin/confd
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 && \  
chmod u+x /bin/confd  
  
ADD ./proxy_params /etc/nginx/proxy_params  
ADD ./config /config  
ADD ./confd /etc/confd  
ADD ./nginx.conf /etc/nginx/nginx.conf  
  
RUN chmod u+x /config/start.sh  
  
WORKDIR /etc/confd  
EXPOSE 80 443  
ENTRYPOINT ["/config/start.sh", "/bin/confd", "-watch", "-log-level", "info",
"-interval=10", "-confdir=/etc/confd", "-backend=etcd"]  
CMD ["-node=127.0.0.1:2379"]  

