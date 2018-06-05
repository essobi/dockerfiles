FROM gliderlabs/alpine:edge  
  
RUN \  
apk --no-cache upgrade \  
&& apk --no-cache add \  
bash \  
openssl \  
curl \  
grep \  
drill \  
coreutils  
  
ENV \  
LE_EMAIL="" \  
LE_RSA_KEY_SIZE=4096 \  
LE_EXTRA_ARGS="" \  
# please change this in production to  
# -e LE_CA="https://acme-v01.api.letsencrypt.org"  
LE_CA="https://acme-staging.api.letsencrypt.org" \  
NS_KEYFILE_PATH="" \  
CLOUDFLARE_EMAIL="" \  
CLOUDFLARE_TOKEN="" \  
LE_VALIDATE_VIA_DNS="false" \  
LE_DNS_ADD_CMD="/usr/local/bin/dns_add_cloudflare" \  
LE_DNS_DEL_CMD="/usr/local/bin/dns_del_cloudflare"  
  
VOLUME /var/acme-webroot/ /.getssl  
  
COPY root/ /  
  
ENTRYPOINT "/getssl.sh"  
CMD ["--help"]  

