FROM fedora:26  
LABEL maintainer="Christopher Antila <christopher@ncodamusic.org>"  
  
COPY scripts/ /tmp/  
RUN /tmp/dnf.sh  
RUN /tmp/node.sh  
  
VOLUME [ "/sys/fs/cgroup", "/tmp", "/run" ]  

