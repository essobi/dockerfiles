FROM fedora:25  
ENV SEMAPHORE_VERSION="2.4.1"  
RUN dnf -q upgrade -y && \  
dnf install -y git ansible mysql openssh-clients python-netaddr && \  
dnf clean all && \  
curl -sSfL "https://github.com/ansible-
semaphore/semaphore/releases/download/v$SEMAPHORE_VERSION/semaphore_linux_amd64"
\  
> /usr/bin/semaphore && \  
chmod +x /usr/bin/semaphore && \  
mkdir -p /etc/semaphore/playbooks && \  
rm -rf /tmp/*  
  
EXPOSE 3000  
ADD ./scripts/docker-startup.sh /usr/bin/semaphore-startup.sh  
  
ENTRYPOINT ["/semaphore-startup.sh"]  
CMD ["/usr/bin/semaphore", "-config", "/etc/semaphore/semaphore_config.json"]  

