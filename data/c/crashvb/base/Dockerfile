FROM ubuntu:16.04  
LABEL maintainer "Richard Davis <crashvb@gmail.com>"  
  
USER root  
  
# Install packages, download files ...  
ADD docker-* entrypoint healthcheck /sbin/  
ADD entrypoint.sh /usr/local/lib/  
RUN docker-apt apt-transport-https ca-certificates curl gettext pwgen wget vim  
  
# Configure: bash profile  
RUN sed --in-place --expression="/^HISTSIZE/s/1000/9999/"
\--expression="/^HISTFILESIZE/s/2000/99999/" /root/.bashrc && \  
echo "set -o vi" >> /root/.bashrc && \  
echo "PS1='\${debian_chroot:+(\$debian_chroot)}\\\\\\\t
\\[\\\\\\\033[0;31m\\]\u\\[\\\\\\\033[00m\\]@\\[\\\\\\\033[7m\\]\h\\[\\\\\\\033[00m\\]
[\w]\\\\\\\n\$ '" >> /root/.bashrc && \  
touch ~/.hushlogin  
  
# Configure: entrypoint, ca-certificates  
RUN mkdir --mode=0755 --parents /etc/entrypoint.d/ /etc/healthcheck.d/
/usr/share/ca-certificates/docker/  
ADD entrypoint.ca-certificates /etc/entrypoint.d/00ca-certificates  
  
HEALTHCHECK CMD /sbin/healthcheck  
  
ENTRYPOINT ["/sbin/entrypoint"]  
CMD ["/bin/bash"]  

