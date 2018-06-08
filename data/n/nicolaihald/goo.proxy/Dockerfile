FROM haproxy:1.6  
MAINTAINER MAINTAINER Nicolai Hald nha@miracle, Benjamin Zarendof
bza@miracle.dk  
  
# Create a system group and user to be used by HAProxy.  
RUN groupadd haproxy && useradd -g haproxy haproxy  
  
# Need to create a directory for HAProxy to be able to `chroot`.  
# This is a security measurement.  
# Refer to http://cbonte.github.io/haproxy-
dconv/configuration-1.5.html#chroot.  
RUN mkdir /var/lib/haproxy  
  
# Now copy required configurations files etc..  
COPY root /  
RUN chmod +x /docker-entrypoint.sh  
  
# default haproxy.conf settings  
ENV \  
STATS_ENABLE=enable \  
STATS_USERNAME=admin \  
STATS_PASSWORD=nimda  
  
EXPOSE 80 443 1936  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]

