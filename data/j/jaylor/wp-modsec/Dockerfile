FROM wordpress:4.9.4-php7.2-apache  
  
# Install ModSecurity  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
libapache2-modsecurity \  
; \  
rm -rf /var/lib/apt/lists/*  
  
# Move, Edit, and Link Files  
RUN mv /etc/modsecurity/modsecurity.conf-recommended
/etc/modsecurity/modsecurity.conf && \  
sed -i 's/SecRuleEngine DetectionOnly/SecRuleEngine On/'
/etc/modsecurity/modsecurity.conf && \  
ln -s /dev/stdout /var/log/apache2/modsec_audit.log  
  
COPY ./modsecurity_custom_rules.conf /etc/modsecurity/  

