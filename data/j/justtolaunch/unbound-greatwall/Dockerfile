FROM alpine  
  
ENV VERSION 1.6.6  
RUN apk add --no-cache python3 \  
wget \  
openssl \  
unbound  
  
RUN pip3 install wget  
  
ADD assets/header.conf /etc/unbound/header.conf  
ADD assets/footer.conf /etc/unbound/footer.conf  
ADD assets/block.py /etc/unbound/block.py  
  
RUN chown -R unbound:unbound /etc/unbound/  
  
USER unbound  
RUN unbound-anchor -a /etc/unbound/root.key ; true  
RUN unbound-control-setup \  
&& wget ftp://FTP.INTERNIC.NET/domain/named.cache -O /etc/unbound/root.hints  
  
USER root  
ADD start.sh /start.sh  
RUN chmod +x /start.sh \  
&& chmod +x /etc/unbound/block.py  
  
EXPOSE 53/udp  
EXPOSE 53  
CMD ["/start.sh"]  

