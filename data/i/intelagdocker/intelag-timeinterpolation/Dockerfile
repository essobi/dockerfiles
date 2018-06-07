# Dockerfile for light-weight data-filter  
FROM openwhisk/dockerskeleton  
  
ENV FLASK_PROXY_PORT 8080  
RUN pip install pymongo  
RUN pip install pytz  
  
### Add source file(s)  
RUN rm /action/exec  
ADD exec /action/  
RUN chmod +x /action/exec  
  
CMD ["/bin/bash", "-c", "cd actionProxy && python -u actionproxy.py"]  

