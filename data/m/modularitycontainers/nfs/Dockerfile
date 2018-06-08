FROM docker.io/fedora:25  
MAINTAINER "James Antill" <james.antill@redhat.com>  
  
RUN dnf install -y --setopt=tsflags=nodocs nfs-utils && \  
dnf install -y --setopt=tsflags=nodocs /usr/bin/pidof && \  
dnf install -y --setopt=tsflags=nodocs python-mako PyYAML && \  
dnf -y clean all  
  
ADD files /files  
  
# mkdir -p /srv/nfs/Demo/  
RUN mkdir -p /srv/nfs  
RUN /files/config.sh  
  
RUN sh -c 'date > /srv/nfs/tst-build'  
EXPOSE 111/udp  
EXPOSE 2049/tcp  
  
# VOLUME ['/var/log', '/srv/nfs']  
# USER nfs  
CMD ["/files/start.sh"]  
  

