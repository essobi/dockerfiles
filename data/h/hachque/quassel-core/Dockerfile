FROM hachque/systemd-none  
MAINTAINER James Rhodes  
  
# Install requirements  
RUN zypper --non-interactive in quassel-core ca-certificates ca-certificates-
mozilla ca-certificates-cacert  
  
# Expose Quassel core on 4242  
EXPOSE 4242  
# Add the start script  
ADD 10-quasselcore /etc/init.simple/10-quasselcore  
  
# Remove /var/lib/quasselcore (so we can detect the  
# lack of a host mapping).  
RUN rmdir /var/lib/quasselcore  
  
# Remove 00-patch so that launching in pre-baked images runs faster  
RUN rm /etc/init.simple/00-patch  
  
# Set /init as the default  
CMD ["/init"]  

