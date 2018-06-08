FROM alpine:3.5  
MAINTAINER Francesco Vezzoli <fvezzoli@iz2vtw.net>  
  
RUN apk add --no-cache --update unbound openssl  
  
COPY unbound.conf /etc/unbound/unbound.conf  
  
RUN unbound-control-setup && \  
wget ftp://FTP.INTERNIC.NET/domain/named.cache -O /etc/unbound/root.hints  
  
RUN chmod ugo+rwx /etc/unbound/  
  
USER unbound  
RUN unbound-anchor -a /etc/unbound/root.key ; true  
USER root  
  
COPY entrypoint.sh /entrypoint.sh  
  
EXPOSE 53/udp  
EXPOSE 53  
ENTRYPOINT ["/entrypoint.sh"]  

