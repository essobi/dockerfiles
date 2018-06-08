# HEADER  
FROM gliderlabs/alpine:3.6  
  
# Install Quagga  
RUN apk-install quagga  
  
# Supervisord  
#ADD supervisord.conf /etc/supervisord.conf  
  
# Configuration files  
VOLUME /etc/quagga  
  
# Expose ports  
EXPOSE 179 2601 2605  
  
# Command  
#RUN cp /usr/share/doc/quagga/examples/zebra.conf.sample
/etc/quagga/zebra.conf \  
# && cp /usr/share/doc/quagga/examples/vtysh.conf.sample
/etc/quagga/vtysh.conf \  
# && cp /usr/share/doc/quagga/examples/bgpd.conf.sample /etc/quagga/bgpd.conf  

