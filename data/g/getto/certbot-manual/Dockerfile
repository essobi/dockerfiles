FROM quay.io/letsencrypt/letsencrypt:latest  
  
RUN pip install awscli  
  
ENV HOME /home/letsencrypt  
  
ENV LETSENCRYPT_CONFIG /etc/letsencrypt  
ENV LETSENCRYPT_LOG /tmp  
ENV LETSENCRYPT_DOMAIN ""  
ENV LETSENCRYPT_EMAIL ""  
ENV AWS_ROUTE53_HOSTED_ZONE_ID ""  
ENTRYPOINT /manual.sh  
  
COPY auth.sh cleanup.sh manual.sh /  

