FROM fedora:24  
  
MAINTAINER Alex Smith <alex.smith@redhat.com>  
  
RUN groupadd -g 1001 carbon-c-relay  
RUN useradd -r -s /sbin/nologin -d /var/lib/carbon-c-relay -u 1001 -g 1001
carbon-c-relay  
  
RUN dnf install -y carbon-c-relay && dnf clean all  
  
WORKDIR /var/lib/carbon-c-relay  
USER carbon-c-relay  
EXPOSE 2003  
CMD ["/usr/bin/carbon-c-relay", "-f", "/etc/carbon-c-relay.conf"]  

