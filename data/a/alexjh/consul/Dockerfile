FROM voxxit/base:alpine  
  
# Replacement for voxxit/consul using a branch with fixes for DNS  
# UDP packet size being too large for go-based programs  
ENV CONSUL_VERSION 0.6.4  
ENV GOPATH /tmp/go  
ENV CONSUL_DIR ${GOPATH}/src/github.com/hashicorp/consul  
  
RUN apk add --update ca-certificates curl git make go zip \  
&& git clone https://github.com/alexjh/consul --branch compress-dns --single-
branch ${CONSUL_DIR} \  
&& make -C ${CONSUL_DIR} tools dev \  
&& cp ${CONSUL_DIR}/bin/consul /bin/ \  
&& mkdir /tmp/ui && cd /tmp/ui \  
&& curl
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_web_ui.zip
-o /tmp/ui.zip \  
&& unzip /tmp/ui.zip \  
&& mkdir /ui \  
&& mv * /ui \  
&& apk del curl git make go zip \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  
  
VOLUME [ "/data" ]  
  
ENTRYPOINT [ "/bin/consul" ]  
  
CMD [ "agent", "-data-dir", "/data" ]  

