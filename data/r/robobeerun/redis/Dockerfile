FROM redis:4.0.4-alpine  
LABEL maintainer "Erwin Mueller <erwin.mueller@deventm.com>"  
  
# Finishing up.  
USER redis  
  
WORKDIR /data  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["redis-server"]  

