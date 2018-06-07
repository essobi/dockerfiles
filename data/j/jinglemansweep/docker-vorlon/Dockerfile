FROM vorlonjs/dashboard:0.5.4  
ADD files /files  
RUN chmod +x /files/entrypoint.sh /files/configure.js  
  
ENTRYPOINT ["/files/entrypoint.sh"]  

