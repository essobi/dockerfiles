# Dockerfile for light-weight data-filter  
FROM openwhisk/dockerskeleton  
  
ENV FLASK_PROXY_PORT 8080  
### Add source file(s)  
RUN mkdir -p /action/maxmins  
ADD f1.py /action/f1.py  
RUN rm /action/exec  
ADD exec /action/  
RUN chmod +x /action/exec  
ADD maxkey.csv /action/maxmins/  
ADD minkey.csv /action/maxmins/  
  
CMD ["/bin/bash", "-c", "cd actionProxy && python -u actionproxy.py"]  

