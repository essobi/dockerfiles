FROM emanueleperuffo/baseimage-debian:latest  
MAINTAINER Emanuele Peruffo <info@emanueleperuffo.com>  
  
ENV HOME /root  
ADD . /build  
  
ENV LDAP_DOMAIN example.com  
ENV LDAP_ORGANIZATION example.com  
ENV LDAP_ADMIN_PASSWORD pass  
  
RUN /build/prepare.sh && \  
/build/services.sh && \  
/build/cleanup.sh  
  
VOLUME ["/var/lib/ldap", "/etc/ldap/slapd.d"]  
  
EXPOSE 389  
CMD ["/sbin/my_init"]

