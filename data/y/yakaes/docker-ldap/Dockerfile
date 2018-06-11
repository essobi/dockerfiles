FROM alpine  
  
RUN \  
apk --no-cache add openldap openldap-back-hdb && \  
mkdir -p /var/lib/openldap-data && \  
cp -a /etc/openldap /etc/openldap.default  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["serve"]  
  

