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
  
CMD "/dehydrated/dehydrated --register --accept-terms -f
/dehydrated/config/config && /dehydrated/dehydrated -f
/dehydrated/config/config -c"  
  
VOLUME /dehydrated/certs  
VOLUME /dehydrated/config  
  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1" \  
org.freenas.upgradeable="false" \  
org.freenas.expose-ports-at-host="false" \  
org.freenas.autostart="false" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/dehydrated/config\", \  
\"descr\": \"Configuration Directory\" \  
}, \  
{ \  
\"name\": \"/dehydrated/certs\", \  
\"descr\": \"Certificate directory\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"CF_EMAIL\", \  
\"descr\": \"Cloudflare - Login email\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"CF_KEY\", \  
\"descr\": \"Cloudflare API key\", \  
\"optional\": false \  
} \  
]"  

