FROM emanueleperuffo/baseimage-debian:latest  
MAINTAINER Emanuele Peruffo <info@emanueleperuffo.com>  
  
ENV HOME /root  
ADD . /build  
  
ENV LDAP_HOST ldap.example.com  
ENV LDAP_BASE_DN dc=example,dc=com  
ENV LDAP_BIND_DN cn=dovecot,dc=example,dc=com  
ENV LDAP_PASS pass  
  
ENV POSTMASTER postmaster@example.com  
ENV LMTP_HOSTNAME dovecot.example.com  
ENV EXPUNGE_TRASH 30d  
ENV EXPUNGE_JUNK 30d  
ENV CRON_EXPUNGE_TRASH 30 0 * * *  
ENV CRON_EXPUNGE_JUNK 40 0 * * *  
  
RUN /build/prepare.sh && \  
/build/services.sh && \  
/build/cleanup.sh  
  
# /etc/ssl/dovecot  
VOLUME ["/mail"]  
  
EXPOSE 12345 143 4190 24  
CMD ["/sbin/my_init"]

