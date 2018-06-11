FROM ubuntu:rolling  
  
ENV S6v=v1.19.1.1  
RUN export DEBIAN_FRONTEND=noninteractive && apt update && apt install -yq
curl ca-certificates busybox dropbear && \  
curl -sOL https://github.com/just-
containers/s6-overlay/releases/download/${S6v}/s6-overlay-amd64.tar.gz && \  
tar xf s6-overlay-amd64.tar.gz && rm s6-overlay-amd64.tar.gz && \  
/bin/busybox --install -s /bin && \  
rm -rf /var/lib/apt/lists  
  
COPY s6-hiercopy /bin/s6-hiercopy  
COPY services.d /etc/services.d  
  
CMD ["/init"]  

