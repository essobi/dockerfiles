FROM alpine:edge  
  
MAINTAINER Ann Arbor District Library <github@aadl.org>  
  
RUN apk add --update --no-cache --repository=https://s3.amazonaws.com/aadl-
github/alpine \  
cups-pdf cups-filters 'cups<2.2.4' \--allow-untrusted && \  
sed -i 's/Listen localhost:631/Listen 0.0.0.0:631/' /etc/cups/cupsd.conf && \  
sed -i 's/<Location \/>/<Location \/>\n Allow All/' /etc/cups/cupsd.conf && \  
sed -i 's/<Location \/admin>/<Location \/admin>\n Allow All\n Require user
@SYSTEM/' /etc/cups/cupsd.conf && \  
sed -i 's/<Location \/admin\/conf>/<Location \/admin\/conf>\n Allow All/'
/etc/cups/cupsd.conf && \  
echo "ServerAlias *" >> /etc/cups/cupsd.conf && \  
echo "DefaultEncryption Never" >> /etc/cups/cupsd.conf  
  
VOLUME /etc/cups/ /var/log/cups /var/spool/cups /var/spool/cups-pdf
/var/cache/cups  
  
COPY start-cups.sh /root/start-cups.sh  
RUN chmod +x /root/start-cups.sh  
  
CMD ["/root/start-cups.sh"]  
  
EXPOSE 631  

