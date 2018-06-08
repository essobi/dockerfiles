FROM debian:jessie  
  
ENV CONSUL_VERSION 0.6.4  
ENV CONSUL_SHA256
abdf0e1856292468e2c9971420d73b805e93888e006c76324ae39416edcf0627  
ENV CONSUL_PACKAGE consul_${CONSUL_VERSION}_linux_amd64.zip  
  
RUN \  
apt-get update &&\  
apt-get install -y unzip  
  
WORKDIR /tmp  
  
ADD https://releases.hashicorp.com/consul/${CONSUL_VERSION}/${CONSUL_PACKAGE}
${CONSUL_PACKAGE}  
  
RUN \  
echo "${CONSUL_SHA256} ${CONSUL_PACKAGE}" > CONSUL_SHA256SUM &&\  
sha256sum --check CONSUL_SHA256SUM &&\  
unzip ${CONSUL_PACKAGE} -d /usr/local/bin &&\  
chmod +x /usr/local/bin/consul  
  
RUN rm -r *  
  
VOLUME ["/data"]  
  
ENTRYPOINT ["consul"]  
  
CMD ["agent", "-server", "-data-dir", "/data", "-client", "0.0.0.0"]  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  

