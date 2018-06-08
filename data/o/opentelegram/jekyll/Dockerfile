FROM jekyll/builder:3.5  
RUN apk --no-cache add sudo  
  
COPY ./entrypoint.sh /usr/bin/entrypoint.sh  
RUN chmod +x /usr/bin/entrypoint.sh  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
  

