FROM alpine:3.4  
ADD
https://github.com/giabao/confd/releases/download/v0.12.0-alpha3.1/confd-0.12.0-alpha3.1-alpine-
amd64 /confd  
RUN chmod +x /confd  
  
ADD ./confd /etc/confd  
  
VOLUME /etc/mosquitto  
  
ENTRYPOINT ["/confd"]  
CMD ["-backend=rancher", "--prefix=/2015-12-19/self/service/metadata",
"-node", "rancher-metadata.rancher.internal"]  

