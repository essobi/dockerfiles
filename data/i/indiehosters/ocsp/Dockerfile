FROM debian:jessie  
  
RUN apt-get update && apt-get install -y \  
cron \  
openssl \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY crontab /etc/cron.d/ocsp  
COPY ocsp.sh /ocsp.sh  
  
CMD [ "cron", "-f" ]  

