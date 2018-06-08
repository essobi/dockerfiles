FROM alpine  
  
RUN apk add dhcp tftp-hpa --no-cache  
RUN touch /var/lib/dhcp/dhcpd.leases  
  
ADD tftproot /tftproot  
RUN chmod 755 /tftproot  
RUN chmod 644 /tftproot/*  
  
ADD dhcpd.conf /etc/dhcpd.conf  
RUN chmod 644 /etc/dhcpd.conf  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
  
CMD [ "/entrypoint.sh" ]  

