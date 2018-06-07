FROM jppgks/http:latest  
  
# Make sure to expose port 8080 where the server runs  
EXPOSE 8080  
WORKDIR server/  
ENTRYPOINT ["/sbin/tini", "--", "sh", "-c", "gradle run", "-q"]  
  

