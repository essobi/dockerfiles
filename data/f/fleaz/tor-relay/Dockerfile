FROM alpine:latest  
LABEL maintainer Felix Breidenstein <mail@fleaz.me>  
  
RUN apk add --update tor  
  
# ORPort, DirPort, SocksPort  
EXPOSE 9001 9030 9050 9051  
VOLUME /var/lib/tor  
VOLUME /etc/tor/torrc  
  
CMD ["/usr/bin/tor"]  

