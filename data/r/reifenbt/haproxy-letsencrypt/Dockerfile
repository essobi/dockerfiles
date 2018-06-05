FROM haproxy:alpine  
  
RUN apk add --no-cache openssl python3 certbot  
  
COPY wrapper.py wrapper.py  
COPY cert.py cert.py  
  
ENTRYPOINT ["python3", "wrapper.py"]  

