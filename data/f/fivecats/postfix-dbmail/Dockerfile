FROM base/archlinux:latest  
  
RUN pacman -Syq --noconfirm archlinux-keyring systemd-sysvcompat \  
&& pacman -Syyuq --noconfirm  
RUN pacman -Sq --noconfirm \  
dbmail \  
libsieve \  
postfix \  
cyrus-sasl \  
cyrus-sasl-ldap \  
syslog-ng \  
json-c \  
librabbitmq-c \  
libmongoc \  
python  
RUN pacman -Sccq --noconfirm  
RUN useradd dbmail \  
&& mkdir -p /var/log/dbmail \  
&& chown dbmail:dbmail /var/run/dbmail /var/log/dbmail  
  
VOLUME /etc/postfix  
VOLUME /var/spool/postfix  
EXPOSE 24 25 143 587 993  
CMD echo "starting servers..." \  
&& syslog-ng \  
&& saslauthd -a ldap \  
&& postfix -c /etc/postfix start \  
&& dbmail-lmtpd \  
&& dbmail-timsieved \  
&& dbmail-imapd -v -D  

