FROM certbot/certbot  
  
RUN pip install certbot-dns-route53  
  
COPY run.sh run.sh  
RUN chmod +x run.sh  
  
ENTRYPOINT ["/opt/certbot/run.sh"]  

