FROM debian:latest  
  
WORKDIR /certs-extractor  
  
ADD
https://raw.githubusercontent.com/containous/traefik/master/contrib/scripts/dumpcerts.sh
./dumpcerts.sh  
ADD ./entrypoint.sh ./entrypoint.sh  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
entr \  
jq \  
openssl \  
util-linux; \  
rm -rf /var/lib/apt/lists/*; \  
chmod +x ./dumpcerts.sh; \  
chmod +x ./entrypoint.sh;  
  
ENTRYPOINT ["./entrypoint.sh"]

