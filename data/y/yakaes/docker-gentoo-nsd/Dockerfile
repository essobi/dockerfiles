  
FROM gentoo/stage3-amd64-hardened  
  
RUN \  
wget -O - --no-verbose "http://distfiles.gentoo.org/snapshots/portage-
latest.tar.bz2" | tar -C /usr -jxf - && \  
mkdir -p /etc/portage/package.keywords && \  
echo "net-dns/nsd ~amd64" > /etc/portage/package.keywords/nsd && \  
env FEATURES="-sandbox -usersandbox" PORTAGE_SSH_OPTS="" emerge -qv net-
dns/nsd && \  
rm -R /usr/portage/*  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD server  
  

