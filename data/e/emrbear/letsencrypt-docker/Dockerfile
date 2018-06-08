FROM quay.io/letsencrypt/letsencrypt:latest  
COPY . .  
ENV CERT_RENEW_ONLY=true  
RUN pip install python-dockercloud  
RUN crontab renew_crontab  
ENTRYPOINT ./start.sh  
EXPOSE 80

