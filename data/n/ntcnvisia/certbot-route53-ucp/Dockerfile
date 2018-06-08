FROM ntcnvisia/certbot-route53  
MAINTAINER dlee@nvisia.com  
  
VOLUME /var/ucp-certs  
  
RUN pip install \  
requests \  
BeautifulSoup  
  
COPY hook-post.sh /root/certbot-route53/hook-post.sh  
COPY getIdenTrustCa.py /root/certbot-route53/getIdenTrustCa.py  
  
RUN chmod +x /root/certbot-route53/hook-post.sh  
  
ENTRYPOINT ["/root/certbot-route53/main.sh"]  

