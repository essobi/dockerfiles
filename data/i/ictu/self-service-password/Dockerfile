FROM phusion/baseimage:0.9.16  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Environment for Apache configuration  
ENV SMTP_HOST="localhost" \  
MAIL_FROM="password-service@example.com" \  
SSL_CERT_PASS="top-secret"  
# Environment for LDAP configuration  
ENV LDAP_URL="ldap://localhost" \  
LDAP_BINDDN="cn=manager,dc=example,dc=com" \  
LDAP_BINDPW="secret" \  
LDAP_BASE="dc=example,dc=com" \  
LDAP_LOGIN_ATTRIBUTE="uid" \  
LDAP_FULLNAME_ATTRIBUTE="cn" \  
LDAP_FILTER="(&(objectClass=person)(${LDAP_LOGIN_ATTRIBUTE}={login}))"  
# Environment for Password Policy  
ENV PWD_MIN_LENGTH=0 \  
PWD_MAX_LENGTH=0 \  
PWD_MIN_LOWER=0 \  
PWD_MIN_UPPER=0 \  
PWD_MIN_DIGIT=0 \  
PWD_MIN_SPECIAL=0 \  
PWD_SPECIAL_CHARS="^a-zA-Z0-9" \  
PWD_NO_REUSE=true \  
PWD_COMPLEXITY=0 \  
PWD_SHOW_POLICY=never \  
PWD_SHOW_POLICY_POS=above  
  
# Install Apache2, PHP and LTB ssp  
RUN apt-get update && \  
apt-get install -y apache2 php5 php5-mcrypt php5-ldap sendmail && \  
apt-get clean && \  
curl http://tools.ltb-project.org/attachments/download/499/self-service-
password_0.8-1_all.deb > self-service-password.deb && \  
dpkg -i self-service-password.deb && \  
rm -f self-service-password.deb  
  
# Configure self-service-password site  
RUN mkdir -p /certs  
ADD assets/self-service-password /etc/apache2/sites-available/self-service-
password  
ADD assets/passphrase.sh /usr/share/self-service-password/conf/passphrase.sh  
RUN ln -s self-service-password /etc/apache2/sites-available/self-service-
password.conf && \  
ln -s ../../mods-available/mcrypt.ini /etc/php5/apache2/conf.d/20-mcrypt.ini
&& \  
a2enmod ssl && a2enmod rewrite && \  
a2dissite 000-default && \  
a2ensite self-service-password  
  
# This is where configuration goes  
ADD assets/config.inc.php /usr/share/self-service-password/conf/config.inc.php  
  
# Add ICTU logo  
ADD assets/ictu-logo.svg /usr/share/self-service-password/style/ictu-logo.svg  
  
# Start Apache2 as runit service  
RUN mkdir /etc/service/apache2  
ADD assets/apache2.sh /etc/service/apache2/run  
  
EXPOSE 80 443  

