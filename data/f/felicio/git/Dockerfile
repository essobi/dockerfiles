FROM felicio/git:git  
LABEL description="Git Server – SSH Protocol"  
  
# Change user back to root since git images exits wit non-privileged user.  
USER root  
  
RUN apt-get update && apt-get install --no-install-recommends -q=2 \  
openssh-server  
  
# Restrict ssh daemon's access outside a directory tree by creating privilige
separation directory (chroot jail).  
RUN mkdir /var/run/sshd  
  
# Configure SSH server.  
COPY ["etc/sshd_config", "/etc/ssh/sshd_config"]  
  
# Test validity of configuration file and output effective configuration.  
RUN sshd -T > /var/log/sshd_test.log  
  
# Mount file containing all permitted users' public keys.  
VOLUME ["/srv/git/private", "/home/git/.ssh/authorized_keys"]  
  
EXPOSE 22  
# sshd re-exec requires execution with an absolute path.  
CMD ["/usr/sbin/sshd", "-D"]  

