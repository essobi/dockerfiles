FROM certbot/certbot  
COPY entry.sh /entryp  
COPY entry-test.sh /test-entryp  
COPY auth.sh /auth  
RUN ln -s /auth /cleanup  
ENTRYPOINT ["/entryp"]  

