FROM debian:jessie  
  
MAINTAINER Anushan Easwaramoorthy <EAnushan@hotmail.com>  
  
# Install packages.  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
wget \  
bzip2 \  
build-essential \  
libssl-dev \  
tcl-dev \  
libxml2-dev \  
libpcre3-dev \  
ssl-cert  
  
# Download Apache Traffic Server.  
RUN cd /opt && wget
http://mirror.csclub.uwaterloo.ca/apache/trafficserver/trafficserver-5.3.0.tar.bz2
&& tar xf trafficserver-5.3.0.tar.bz2 && cd trafficserver-5.3.0 && ./configure
&& make && make install  
  
# Configure dynamic linker.  
RUN ldconfig  
  
# Configuration.  
RUN sed -i 's/\\(CONFIG proxy.config.http.server_ports STRING\\).*$/\1 80
443:ssl/g' /usr/local/etc/trafficserver/records.config  
RUN echo "dest_ip=* ssl_cert_name=ssl-cert-snakeoil.pem ssl_key_name=ssl-cert-
snakeoil.key" >> /usr/local/etc/trafficserver/ssl_multicert.config  
RUN echo "CONFIG proxy.config.ssl.server.cert.path STRING /etc/ssl/certs/" >>
/usr/local/etc/trafficserver/records.config  
RUN echo "CONFIG proxy.config.ssl.server.private_key.path STRING
/etc/ssl/private/" >> /usr/local/etc/trafficserver/records.config  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  
# Copy startup script.  
COPY trafficserver-foreground /usr/local/bin/  
  
# Start!  
CMD ["trafficserver-foreground"]

