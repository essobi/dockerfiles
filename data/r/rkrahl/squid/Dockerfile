FROM rkrahl/opensuse  
  
RUN zypper --non-interactive install \  
squid && \  
sed -i -e 's/^\\#\\(cache_dir aufs .*\\)/\1/' /etc/squid/squid.conf && \  
/usr/sbin/squid -z -F -N -S -f /etc/squid/squid.conf  
  
CMD ["/usr/sbin/squid", "-F", "-sY", "/etc/squid/squid.conf"]  
  
EXPOSE 3128  

