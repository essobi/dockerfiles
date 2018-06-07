FROM python:alpine  
LABEL maintainer="indrek@ardel.eu"  
  
ADD dehydrated /etc/periodic/daily/dehydrated  
RUN apk add --update curl openssl bash git && \  
cd / && \  
git clone https://github.com/lukas2511/dehydrated && \  
cd dehydrated && \  
mkdir hooks && \  
git clone https://github.com/kappataumu/letsencrypt-cloudflare-hook
hooks/cloudflare && \  
pip install -r hooks/cloudflare/requirements.txt && \  
apk del git && \  
rm -rf /var/cache/apk/* /tmp/* /var/tmp/ && \  
chmod +x /etc/periodic/daily/dehydrated && \  
touch /dehydrated/domains.txt  
  
CMD /etc/periodic/daily/dehydrated && crond -f  
  
VOLUME /dehydrated/certs  

