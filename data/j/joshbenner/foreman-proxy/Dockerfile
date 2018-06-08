# FROM phusion/baseimage:0.9.20  
FROM ubuntu:16.04  
  
ENV FOREMAN_RELEASE=1.14 \  
FOREMAN_PACKAGE_VERSION=1.14.2-1 \  
DOCKERIZE_VERSION=v0.3.0 \  
SSL=false \  
FOREMAN_URL=foreman \  
TRUSTED_HOSTS=localhost,host1,host2 \  
BMC_ENABLED=true \  
BMC_DEFAULT_PROVIDER=freeipmi \  
REALM_ENABLED=false \  
IPA_KEYTAB_PATH=/etc/foreman-proxy/freeipa.keytab \  
IPA_PRINCIPAL=realm-proxy@EXAMPLE.COM \  
IPA_CONFIG_PATH=/etc/ipa/default.conf \  
IPA_REMOVE_DNS=true \  
DHCP_ENABLED=false \  
DHCP_PROVIDER=dhcp_isc \  
DHCP_SERVER=dhcp \  
ISC_DHCP_CONFIG_PATH=/etc/dhcp/dhcpd.conf \  
ISC_DHCP_LEASES_PATH=/var/lib/dhcp/dhcpd.leases \  
ISC_DHCP_OMAPI_PORT=7911 \  
ISC_DHCP_OMAPI_KEY=omapi_key \  
ISC_DHCP_OMAPI_SECRET=changeme \  
TFTP_ENABLED=false \  
TFTP_ROOT=/var/lib/tftpboot \  
TFTP_SERVERNAME=tftp.localdomain \  
DNS_ENABLED=false \  
DNS_PROVIDER=dns_nsupdate \  
DNS_TTL=86400 \  
NSUPDATE_KEY_PATH=/etc/bind/rndc.key \  
NSUPDATE_SERVER=dns.localdomain \  
LOGS_ENABLED=true  
# Install dockerize  
RUN apt-get update && \  
apt-get install -y ca-certificates wget && \  
wget -q
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz &&
\  
rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Install Foreman proxy  
RUN wget -q https://deb.theforeman.org/pubkey.gpg -O- | apt-key add - && \  
echo "deb http://deb.theforeman.org/ xenial $FOREMAN_RELEASE" >
/etc/apt/sources.list.d/foreman.list && \  
echo "deb http://deb.theforeman.org/ plugins $FOREMAN_RELEASE" >>
/etc/apt/sources.list.d/foreman.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y -q \  
foreman-proxy=$FOREMAN_PACKAGE_VERSION \  
dnsutils freeipmi ipmitool isc-dhcp-server && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
COPY files/ /  
  
# ENTRYPOINT ["/sbin/my_init"]  
ENTRYPOINT ["/entrypoint.sh"]  

