FROM mongo:3.2  
#to be used as version for pushing the image in a jenkins job  
ENV mongo_repl_util_version 0.1  
COPY start.sh /start.sh  
  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  

