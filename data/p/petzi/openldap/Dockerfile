FROM alpine:3.7  
RUN apk add --no-cache openldap-clients openldap openldap-back-mdb openldap-
overlay-all  
  
EXPOSE 389  
VOLUME /var/lib/openldap /var/log/openldap  
  
# Copy the entrypoint script  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
  
# Copy the setup script and prepare the mount points  
COPY setup.sh /setup.sh  
RUN chmod u+x /setup.sh  
RUN mkdir -p /setup/conf.dist  
RUN mkdir -p /setup/ldif.dist  
COPY conf.dist/* /setup/conf.dist/  
COPY ldif.dist/* /setup/ldif.dist/  
  
ONBUILD COPY conf/ /setup/conf/  
ONBUILD COPY ldif/ /setup/ldif/  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [ "/usr/sbin/slapd", "-u", "ldap", "-g", "ldap", "-F",
"/etc/openldap/slapd.d", "-d", "256"]  

