FROM fedora:24  
MAINTAINER Victor Romero <victor.romero@gmail.com>  
  
# add user and group for artemis  
RUN groupadd -r quiver && useradd -r -g quiver quiver  
  
RUN dnf install -y 'dnf-command(copr)' && \  
dnf copr enable -y jross/ssorj && \  
dnf install -y qpid-proton-c && \  
dnf install -y quiver  
  
USER quiver  
ENTRYPOINT ["/usr/bin/quiver"]  

