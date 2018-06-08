#  
# Extends catatnight/postfix by specializing mail logging and allowing a
whitelist of addresses to send to  
#  
FROM catatnight/postfix:latest  
  
# Isolate postfix logs so we can mount a volume to extract them from the
container  
RUN mkdir /var/log/mail && \  
chown syslog:adm /var/log/mail && \  
sed -i "s|/var/log/mail.log|/var/log/mail/mail.log|"
/etc/rsyslog.d/50-default.conf  
  
# Override install script to insert our own extra configuration options  
COPY install.sh /opt/install.sh  
# Prepare a recipient whitelist that allows sending to everybody by default  
COPY recipient_whitelist /etc/postfix/recipient_whitelist  

