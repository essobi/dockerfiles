FROM alpine:3.7  
COPY brian.woolstrum@gmail.com-5a7691ec.rsa.pub /etc/apk/keys  
RUN sed -i '$ ahttp://alpine.woolstrum.net/testing\n' /etc/apk/repositories  
RUN apk update && \  
apk add --no-cache kea-dhcp4  
  
RUN sed -i "s,/tmp/kea-dhcp4-ctrl.sock,/var/kea/kea/kea-dhcp4-ctrl.sock,g"
/etc/kea/kea-*.conf  
RUN sed -i 's/\\("interfaces":\\) \\[ \\]/\1 [ "*" ]/' /etc/kea/kea-dhcp4.conf  
  
EXPOSE 67  
EXPOSE 67/udp  
  
VOLUME /var/kea/kea  
VOLUME /etc/kea  
  
CMD ["/usr/sbin/kea-dhcp4","-c","/etc/kea/kea-dhcp4.conf"]  

