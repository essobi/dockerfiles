FROM python:latest  
  
RUN apt-get update && \  
apt-get install -y curl sed grep mktemp git && \  
cd / && \  
git clone https://github.com/lukas2511/dehydrated && \  
cd dehydrated && \  
mkdir config && \  
mkdir hooks && \  
git clone https://github.com/kappataumu/letsencrypt-cloudflare-hook
hooks/cloudflare && \  
pip install -r hooks/cloudflare/requirements.txt && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/  
  
WORKDIR /dehydrated  
  
CMD ./dehydrated --register --accept-terms -f ./config/config && ./dehydrated
-f ./config/config -c  
  
VOLUME /dehydrated/certs  
VOLUME /dehydrated/config  

