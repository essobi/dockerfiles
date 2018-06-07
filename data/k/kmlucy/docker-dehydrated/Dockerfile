FROM python:3-alpine3.4  
LABEL maintainer "Kyle Lucy <kmlucy@gmail.com>"  
  
RUN apk add --update curl openssl bash git && \  
cd / && \  
git clone https://github.com/lukas2511/dehydrated && \  
cd dehydrated && \  
mkdir hooks && \  
git clone https://github.com/kappataumu/letsencrypt-cloudflare-hook
hooks/cloudflare && \  
pip install -r hooks/cloudflare/requirements.txt && \  
apk del git && \  
rm -rf /var/cache/apk/* /tmp/* /var/tmp/  
  
WORKDIR /dehydrated  
  
CMD ./dehydrated --register --accept-terms && ./dehydrated -c -d $CF_HOST -t
dns-01 -k 'hooks/cloudflare/hook.py'  
  
VOLUME /dehydrated/certs  

