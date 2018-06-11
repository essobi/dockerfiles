  
FROM gentoo/stage3-amd64-hardened  
  
RUN \  
wget -O - --no-verbose "http://distfiles.gentoo.org/snapshots/portage-
latest.tar.bz2" | tar -C /usr -jxf - && \  
env FEATURES="-sandbox -usersandbox" PORTAGE_SSH_OPTS="" emerge -qv net-
nds/openldap && \  
rm -R /usr/portage/*  
  
RUN cp -a /etc/openldap /etc/openldap.default  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["server"]  
  

