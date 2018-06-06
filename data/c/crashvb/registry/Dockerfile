FROM registry:2.3  
MAINTAINER Richard Davis <crashvb@gmail.com>  
  
USER root  
  
# Install packages, download files ...  
ADD docker-* entrypoint /sbin/  
RUN docker-apt gettext pwgen wget  
  
# Configure: bash profile  
RUN sed --in-place "s/HISTSIZE=1000/HISTSIZE=9999/g" /root/.bashrc && \  
sed --in-place "s/HISTFILESIZE=2000/HISTFILESIZE=99999/g" /root/.bashrc && \  
echo "# --- Docker Bash Profile ---" >> /root/.bashrc && \  
echo "set -o vi" >> /root/.bashrc && \  
echo "PS1='\${debian_chroot:+(\$debian_chroot)}\\\\\\\t
\\[\\\\\\\033[0;31m\\]\u\\[\\\\\\\033[00m\\]@\\[\\\\\\\033[7m\\]\h\\[\\\\\\\033[00m\\]
[\w]\\\\\\\n\$ '" >> /root/.bashrc && \  
touch ~/.hushlogin  
  
# Configure: registry  
ENV REGISTRY_HOME=/var/lib/registry  
ENV REGISTRY_AUTH=htpasswd
REGISTRY_AUTH_HTPASSWD_PATH=${REGISTRY_HOME}/.htpasswd
REGISTRY_AUTH_HTPASSWD_REALM=Registry\ Secure\ Access  
  
# Configure: entrypoint  
RUN mkdir \--mode=0755 --parents /etc/entrypoint.d/  
ADD entrypoint.registry /etc/entrypoint.d/registry  
  
ENTRYPOINT ["/sbin/entrypoint"]  
CMD ["/bin/registry", "/etc/docker/registry/config.yml"]  

