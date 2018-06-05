FROM wernight/ngrok  
  
COPY smartweb-entrypoint.sh /  
  
USER root  
RUN chmod +x /smartweb-entrypoint.sh  
USER ngrok  
  
ENTRYPOINT ["/smartweb-entrypoint.sh"]  

