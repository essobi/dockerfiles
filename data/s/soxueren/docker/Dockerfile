FROM docker:latest  
  
ADD server.crt /server.crt  
RUN cat /server.crt >> /etc/ssl/certs/ca-certificates.crt  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["sh"]  

