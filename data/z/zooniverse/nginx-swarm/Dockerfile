FROM zooniverse/apps-nginx  
  
COPY openfaas.conf /etc/nginx-sites/  
  
HEALTHCHECK \--interval=1m30s --timeout=10s --retries=3 --start-period=5m \  
CMD curl -f http://localhost  

