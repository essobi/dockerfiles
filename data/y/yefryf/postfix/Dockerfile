FROM ubuntu:latest  
#  
# # File Author / Maintainer  
  
MAINTAINER Yefry Figueroa  
# Set to no tty  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8  
  
RUN apt-get update && \  
apt-get -y dist-upgrade  
  
# install postfix  
RUN echo "postfix postfix/main_mailer_type select smarthost" | debconf-set-
selections && \  
echo "postfix postfix/mailname string localhost" | debconf-set-selections && \  
echo "postfix postfix/mynetworks select 10.0.0.0/8" | debconf-set-selections
&& \  
echo "postfix postfix/mynetworks select 10.0.0.0/8 172.17.0.0/16" | debconf-
set-selections && \  
apt-get update && apt-get install -y postfix telnet vim  
  
# install clamav  
RUN apt-get install -y clamav-daemon clamav-freshclam  
  
# install rspamd & rmilter  
RUN apt-get install -y lsb-release wget git && \  
wget -O- https://rspamd.com/apt-stable/gpg.key | apt-key add - && \  
export CODENAME=`lsb_release -c -s` && echo "deb http://rspamd.com/apt-stable/
$CODENAME main" > /etc/apt/sources.list.d/rspamd.list && \  
export CODENAME=`lsb_release -c -s` && echo "deb-src http://rspamd.com/apt-
stable/ $CODENAME main" >> /etc/apt/sources.list.d/rspamd.list && \  
apt-get update && \  
apt-get \--no-install-recommends install -y rspamd rmilter && \  
touch /etc/rspamd/rspamd.conf.local  
  
# config rmilter  
RUN postconf -e "smtpd_milters = unix:/var/run/rmilter/rmilter.sock" && \  
postconf -e "milter_protocol = 6" && \  
postconf -e "milter_mail_macros = i {mail_addr} {client_addr} {client_name}
{auth_authen}" && \  
postconf -e "milter_default_action = accept" && \  
postconf -e "compatibility_level = 2"  
COPY rmilter.conf.local /etc/  
  
# config clamav-sigs sanesecurity  
RUN apt-get install -y dnsutils host supervisor && \  
cd /usr/local/src && \  
git clone https://github.com/extremeshok/clamav-unofficial-sigs.git && \  
cd /usr/local/src/clamav-unofficial-sigs && \  
cp clamav-unofficial-sigs.sh /usr/local/bin/ && \  
chmod 775 /usr/local/bin/clamav-unofficial-sigs.sh && \  
mkdir /etc/clamav-unofficial-sigs/ && \  
touch /var/log/mail.log && \  
cp config/* /etc/clamav-unofficial-sigs/ && \  
mkdir -p /var/log/clamav-unofficial-sigs/ && \  
mv /etc/clamav-unofficial-sigs/os.ubuntu.conf /etc/clamav-unofficial-
sigs/os.conf && \  
sed -i 's/setmode="yes"/setmode="no"/' /etc/clamav-unofficial-sigs/master.conf
&& \  
sed -i
's/#user_configuration_complete="yes"/user_configuration_complete="yes"/'
/etc/clamav-unofficial-sigs/user.conf && \  
sed -i 's/malwarepatrol_receipt_code="YOUR-RECEIPT-
NUMBER"/malwarepatrol_receipt_code="f1455699884"/' /etc/clamav-unofficial-
sigs/master.conf && \  
sed -i 's/securiteinfo_authorisation_signature="YOUR-SIGNATURE-
NUMBER"/securiteinfo_authorisation_signature="e94819c0ac4d80d075e4c70908ec9b05bb545899338a005278946260bb73be66986b52d88b69fbc45038cb97caf614d3d958855777db94e831c95c2b84a8d31a"/'
/etc/clamav-unofficial-sigs/master.conf && \  
/usr/local/bin/clamav-unofficial-sigs.sh \--install-cron && \  
/usr/local/bin/clamav-unofficial-sigs.sh \--install-logrotate && \  
/usr/local/bin/clamav-unofficial-sigs.sh \--install-man && \  
apt-get \--yes --force-yes --no-install-recommends install rsyslog && \  
sed -i 's/\/var\/log\/mail/\/var\/log\/postfix\/mail/'
/etc/rsyslog.d/50-default.conf  
#RUN bash /usr/local/bin/clamav-unofficial-sigs.sh  
  
#Enable TLS encrypt emails  
RUN echo "#Enable TLS encrypt on postfix" >> /etc/postfix/main.cf && \  
echo "smtpd_tls_security_level = may" >> /etc/postfix/main.cf && \  
echo "smtp_tls_security_level = may" >> /etc/postfix/main.cf && \  
echo "smtp_tls_loglevel = 1" >> /etc/postfix/main.cf && \  
echo "smtpd_tls_loglevel = 1" >> /etc/postfix/main.cf && \  
echo "#END - TLS encrypt on postfix" >> /etc/postfix/main.cf  
  
COPY start.sh /start.sh  
COPY postfix.sh /postfix.sh  
  
COPY resolv.conf /etc/resolv.conf  
  
RUN chmod +x /postfix.sh && \  
cp -f /etc/services /var/spool/postfix/etc/services  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 25  
  
CMD /usr/bin/echo myhostname=$myhostname >> /etc/postfix/main.cf;
/usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf  

