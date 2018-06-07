FROM debian:jessie  
  
MAINTAINER mzp <qiuranke@gmail.com>  
  
# mail server information  
ENV MAILHUB smtp.gmail.com:587  
ENV AUTH_USER username  
ENV AUTH_PASS password  
  
# ldap server information  
ENV LDAP_URI ldap://localhost:389  
ENV LDAP_ROOTDN cn=admin,dc=example,dc=com  
ENV LDAP_ROOTPW password  
ENV LDAP_SEARCHBASE ou=accounts,dc=example,dc=com  
  
# Policy expire day  
ENV PWD_EXPIRE_DAY 7  
ENV PWD_MAX_AGE 90  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gawk ldap-utils mailutils ssmtp && rm -rf /var/lib/apt/lists/*  
  
COPY ssmtp_custom.conf /etc/ssmtp/  
COPY mail.template /usr/local/bin/  
COPY entrypoint.sh /usr/local/bin/  
COPY pwdExpiredDay.sh /usr/local/bin/  
  
ENTRYPOINT ["sh","/usr/local/bin/entrypoint.sh"]  
  
VOLUME ["/var/log/pwdExpiredDay"]  

