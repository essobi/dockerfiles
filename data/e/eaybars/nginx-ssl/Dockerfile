FROM eaybars/nginx  
  
# install certbot to obtain ssl certificate from Lets Encrypt  
RUN yum install -y certbot && \  
yum clean all  
  
# Generate Strong Diffie-Hellman Group  
RUN openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048  
  
# override main configuration file  
COPY well-known.conf /etc/nginx/default.d/  
COPY http-root.conf /etc/nginx/archive.d/  
  
# Define entrypoint for the image  
ENTRYPOINT ["/usr/bin/nginx-entrypoint.sh"]  
  
EXPOSE 443  
# Add entrypoint scipt  
COPY nginx-entrypoint.sh /usr/bin  
RUN chmod 777 /usr/bin/nginx-entrypoint.sh  
  
CMD ["--renew-all", "--configure-from-env", "--create-nginx-conf", "missing",
"--run"]  
  

