FROM alpine  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
CMD [ "127.0.0.1" ]  
  
# Add some debuggability  
COPY Dockerfile /  

