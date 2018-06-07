FROM jppgks/http:latest  
  
WORKDIR client/  
  
ENTRYPOINT ["/sbin/tini", "--", "gradle", "run", "-q"]  
CMD ["-Pmethod=GET", "-Phost=localhost", "-Pport=8080"]  
  

