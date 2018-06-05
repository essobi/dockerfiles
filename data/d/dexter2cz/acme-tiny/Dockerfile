FROM debian:latest  
  
# docker run -td -e NAMES=`hostname -f` -p 80:80 -v /root/certs:/acme-
tiny/certs -v /var/www/html/challenges:/var/www/html/.well-known/acme-
challenge --name acme dexter2cz/acme-tiny-docker  
# -e NOAPACHE=1 - run without apache  
# Alias "/.well-known/acme-challenge/" "/var/www/html/challenges/"  
MAINTAINER Pavel Vondruska <vondruska@cesnet.cz>  
  
WORKDIR /acme-tiny  
  
ENV builddeps="ca-certificates curl git openssl apache2 wget python"  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
$builddeps \  
&& rm -r /var/lib/apt/lists/* \  
&& apt-get clean  
  
RUN git clone https://github.com/diafygi/acme-tiny /acme-tiny/acme-tiny  
  
COPY get_cert.sh /acme-tiny/  
COPY gen_csr.sh /acme-tiny/  
COPY start.sh /  
  
ENTRYPOINT ["/start.sh"]  
  

