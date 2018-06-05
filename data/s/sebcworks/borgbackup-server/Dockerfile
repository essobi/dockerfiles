# Will mainly launch the ssh server in foreground  
FROM sebcworks/borgbackup-base  
  
MAINTAINER Sebastien Collin <sebastien.collin@sebcworks.fr>  
  
# Remove Password authentication and disable root login from ssh configuration  
RUN sed -i -e 's/^#PasswordAuthentication yes$/PasswordAuthentication no/g' \  
-e 's/^PermitRootLogin without-password$/PermitRootLogin no/g' \  
/etc/ssh/sshd_config  
  
EXPOSE 22  
COPY docker-borg-server-entrypoint.sh /borg-server.sh  
  
ENTRYPOINT ["/borg-server.sh"]  
CMD ["start"]  

