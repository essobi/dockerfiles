FROM nginx:1.9.9  
COPY entrypoint /opt/entrypoint  
COPY configure /opt/configure  
RUN chmod 755 /opt/entrypoint  
RUN chmod 755 /opt/configure  
  
ENTRYPOINT ["/opt/entrypoint"]  
  
CMD ["nginx", "-g", "daemon off;"]  
  

