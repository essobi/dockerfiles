FROM neighborhoods/nginx-auth-ldap:1.0  
COPY setup.sh /setup.sh  
RUN /setup.sh  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["nginx"]  
  
EXPOSE 80  

