# @link https://github.com/andyshinn/docker-dnsmasq/blob/master/Dockerfile  
FROM alpine:3.4  
RUN apk --no-cache add dnsmasq  
RUN sed -i -e 's/^#address=\/double-
click.net\/127.0.0.1/address=\/dev\/127.0.0.1/' /etc/dnsmasq.conf  
RUN sed -i -e 's/^#address=\/double-
click.net\/127.0.0.1/address=\/test\/127.0.0.1\naddress=\/dev\/127.0.0.1/'
/etc/dnsmasq.conf  
EXPOSE 53 53/udp  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s /usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards
compat  
#ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD ["dnsmasq", "-k", "--resolv-file=/etc/resolv.conf"]  

