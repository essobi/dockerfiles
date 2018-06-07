# Dockerfile for light-weight data-filter  
FROM openwhisk/dockerskeleton  
  
ENV FLASK_PROXY_PORT 8080  
### Add source file(s)  
ADD filter.py /action/  
RUN rm /action/exec  
ADD exec /action/  
RUN chmod +x /action/exec  
  
CMD ["/bin/bash", "-c", "cd actionProxy && python -u actionproxy.py"]  

