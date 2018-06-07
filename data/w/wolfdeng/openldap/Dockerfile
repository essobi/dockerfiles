FROM wolfdeng/alpine:3.6  
MAINTAINER Tony Deng ( wolf.deng@gmail.com )  
  
ENV OPENLDAP_VERSION 2.4.44-r0  
  
RUN apk update \  
&& apk add openldap \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 389  
VOLUME ["/etc/openldap-dist","/var/lib/openldap"]  
  
COPY modules/ /etc/openldap/modules  
COPY scripts/* /usr/local/bin/  
  
RUN chmod -R 755 /usr/local/bin/*  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
CMD ["slapd","-d","32789","-u","ldap","-g","ldap"]  

