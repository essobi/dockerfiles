FROM debian:9  
ARG APT_PROXY  
RUN set -x && \  
[ -z "$APT_PROXY" ] || \  
/bin/echo -e "Acquire::HTTP::Proxy \"$APT_PROXY\";\nAcquire::HTTPS::Proxy
\"$APT_PROXY\";\nAcquire::http::Pipeline-Depth \"23\";" > \  
/etc/apt/apt.conf.d/01proxy  
  
RUN set -x && \  
apt-get update -q && \  
apt-get install -qy openvpn iptables curl systune procps tcpdump netcat-
traditional && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/*  
  
ADD ./bin /bin  
RUN chmod +x /bin/*  
EXPOSE 1194/udp  
ENV CONF_DIR /conf  
ENV CERTS_DIR /certs  
  
VOLUME $CONF_DIR $CERTS_DIR  
  
WORKDIR $CONF_DIR  
  
CMD /bin/ovpn_run  
  
HEALTHCHECK CMD nc -uz 127.0.0.1 1195  

