FROM debian:jessie  
ENV DEBIAN_FRONTEND noninteractive  
MAINTAINER miguillo  
  
# Install mercurial-server (and curl for simple HTTP hooks)  
# Clean up SSH keys generated at installation (avoid same keys for every
installations)  
RUN apt-get update -q -q && \  
apt-get install -q -q -y mercurial-server curl && \  
rm -rf /var/lib/apt/lists/* && mkdir -p /var/lib/apt/lists/partial && \  
rm -v /etc/ssh/ssh_host_* && \  
mkdir -v -m 0700 /var/run/sshd  
  
# Install Mutable History For Mercurial  
RUN hg clone https://www.mercurial-scm.org/repo/evolve/ /var/lib/mercurial-
server/mutable-history  
ENV EVOLVE_HASH mercurial-3.1  
RUN hg pull -R /var/lib/mercurial-server/mutable-history && \  
hg up -r $EVOLVE_HASH -R /var/lib/mercurial-server/mutable-history && \  
chown -R hg: /var/lib/mercurial-server/mutable-history  
# Config mercurial-server  
VOLUME ["/var/lib/mercurial-server/repos"]  
EXPOSE 2222  
WORKDIR /var/lib/mercurial-server/  
  
COPY start-mercurial-server.sh /start-mercurial-server.sh  
CMD ["/start-mercurial-server.sh"]  
  
# Allow config of Diffie–Hellman moduli  
RUN mv /etc/ssh/moduli /etc/ssh/moduli.orig && \  
ln -s /var/lib/mercurial-server/repos/sshd_keys/moduli /etc/ssh/moduli  
# Config Mutable History  
ADD evolve.rc /etc/mercurial/hgrc.d/  
ADD evolve.rc /etc/mercurial-server/remote-hgrc.d/  
  
# Running SSH server as normal user  
RUN chown -R hg: /etc/mercurial-server  
USER hg  

