#  
# Dockerfile  
#  
FROM alpine:latest  
  
RUN \  
echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk --no-progress --no-cache add \  
postfix postfix-ldap policyd-spf-fs supervisor \  
opendkim@testing perl openssl  
  
COPY files/entrypoint.sh /entrypoint.sh  
COPY files/opendkim-wrapper.sh /usr/bin/opendkim-wrapper.sh  
COPY files/postfix-wrapper.sh /usr/bin/postfix-wrapper.sh  
COPY files/supervisord.conf /etc/supervisord.conf  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["server"]  
  

