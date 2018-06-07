FROM codingwell/rpi-raspbian-qemu  
  
#  
# Do map these locations:  
# /var/mail/vhosts  
# /var/mail/dovecot-users  
#  
# AUTH PORT: 12345  
# LMTP Port: 24  
# Set Environment  
ENV \  
DEBIAN_FRONTEND=noninteractive \  
DOMAIN=example.com \  
DOVECOT_SSL_CERT_PATH=</etc/dovecot/dovecot.pem \  
DOVECOT_SSL_CERT_KEY=</etc/dovecot/private/dovecot.pem \  
VMAILUSER_ID=5000 \  
POSTMASTER=postmaster@example.com  
  
RUN [ "cross-build-start" ]  
  
COPY assets/bin/ /bin/  
# Start editing  
# Install package here for cache  
RUN apt-get update && apt-get -y install --no-install-recommends \  
ca-certificates \  
dovecot-imapd \  
dovecot-lmtpd \  
dovecot-sqlite \  
rsyslog && \  
cp -r /etc/dovecot/conf.d /etc/dovecot/conf.d.bak && \  
cd /usr/share/dovecot && ./mkcert.sh && \  
chmod a+x /bin/*.sh && chmod a+x /bin/confset && touch /var/mail/dovecot-users
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY assets/etc/dovecot /etc/dovecot/  
  
RUN [ "cross-build-end" ]  
  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["dovecot", "-F"]  

