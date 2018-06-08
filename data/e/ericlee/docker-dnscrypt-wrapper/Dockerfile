FROM debian:wheezy  
  
MAINTAINER Eric Lee "eric.lee.ltk@gmail.com"  
COPY lib/libevent-2.0.so.5 lib/libsodium.so.17 /usr/lib/  
COPY bin/dnscrypt-wrapper /usr/bin/  
COPY bin/run.sh /  
  
VOLUME ["/usr/local/share/dnscrypt-wrapper"]  
  
EXPOSE 443  
EXPOSE 443/udp  
  
CMD ["/run.sh"]  

