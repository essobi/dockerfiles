FROM tmaczukin/debian  
MAINTAINER Tomasz Maczukin "tomasz@maczukin.pl"  
# Install OpenLDAP  
RUN apt-get install -y slapd ldap-utils && apt-get clean  
  
COPY assets/init /usr/local/sbin/init  
RUN chmod 700 /usr/local/sbin/init && chown root:root /usr/local/sbin/init  
  
ENV LDAP_ROOTPASS root  
ENV LDAP_DOMAIN example.com  
ENV LDAP_ORGANIZATION example.com  
  
VOLUME ["/var/lib/ldap"]  
VOLUME ["/etc/ldap/slapd.d"]  
  
EXPOSE 389  
ENTRYPOINT ["/usr/local/sbin/init"]  
CMD ["start"]  
  

