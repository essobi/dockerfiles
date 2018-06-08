FROM fedora:22  
RUN dnf install -y shorewall && \  
dnf clean all  
  
RUN touch /var/log/messages  
  
ENTRYPOINT ["/usr/sbin/shorewall"]  

