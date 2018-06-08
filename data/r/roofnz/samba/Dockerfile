FROM ubuntu:16.04  
MAINTAINER Graeme Gellatly <graemeg@roof.co.nz>  
  
ENV DIRECTORY your.ad.domain  
ENV CLIENT_ID secret  
  
# Install samba  
RUN export DEBIAN_FRONTEND='noninteractive' && \  
apt-get update -qq && \  
apt-get install -qqy --no-install-recommends samba \  
$(apt-get -s dist-upgrade|awk '/^Inst.*ecurity/ {print $2}') &&\  
apt-get install -qqy libnss-ldap ldap-utils nodejs nodejs-legacy npm wget &&\  
useradd -c 'Samba User' -d /tmp -M -r smbuser && \  
sed -i 's|^\\( log file = \\).*|\1/dev/stdout|' /etc/samba/smb.conf && \  
sed -i 's|^\\( unix password sync = \\).*|\1no|' /etc/samba/smb.conf && \  
sed -i '/Share Definitions/,$d' /etc/samba/smb.conf && \  
echo ' security = user' >>/etc/samba/smb.conf && \  
echo ' directory mask = 0775' >>/etc/samba/smb.conf && \  
echo ' force create mode = 0664' >>/etc/samba/smb.conf && \  
echo ' force directory mode = 0775' >>/etc/samba/smb.conf && \  
echo ' force user = smbuser' >>/etc/samba/smb.conf && \  
echo ' force group = users' >>/etc/samba/smb.conf && \  
echo ' load printers = no' >>/etc/samba/smb.conf && \  
echo ' printing = bsd' >>/etc/samba/smb.conf && \  
echo ' printcap name = /dev/null' >>/etc/samba/smb.conf && \  
echo ' disable spoolss = yes' >>/etc/samba/smb.conf && \  
echo ' encrypt_passwords = no' >>/etc/samba/smb.conf && \  
echo '' >>/etc/samba/smb.conf && \  
apt-get clean && \  
auth-client-config -t nss -p lac_ldap && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
COPY aad-login_0.1.tar.gz /opt/  
COPY aad-login /usr/local/bin/  
# Install aad-login  
RUN cd /opt && \  
tar xzf aad-login_0.1.tar.gz -C / && \  
cd /opt/aad-login && \  
npm install && \  
chmod +x /usr/local/bin/aad-login && \  
sed -i.bak "s|var directory = '';|var directory = ${DIRECTORY};|" aad-login.js
&& \  
sed -i "s|var client_id = '';|var client_id = ${CLIENT_ID};|" aad-login.js  
  
RUN cd /etc/pam.d/ && \  
sed -i.bak '\|^$|a auth sufficient pam_exec.so expose_authtok
/usr/local/bin/aad-login' common-auth  
  
COPY samba.sh /usr/bin/  
  
VOLUME ["/etc/samba"]  
  
EXPOSE 137 139 445  
ENTRYPOINT ["samba.sh"]

