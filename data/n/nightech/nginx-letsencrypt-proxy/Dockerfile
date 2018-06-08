FROM nginx  
  
RUN awk '$1 ~ "^deb" { $3 = $3 "-backports"; print; exit }'
/etc/apt/sources.list > /etc/apt/sources.list.d/backports.list && \  
apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 && \  
apt-get update && \  
apt-get install -y --no-install-recommends certbot -t jessie-backports && \  
apt-get install -y --no-install-recommends python-dnspython && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/ && \  
mkdir -p /var/www/letsencrypt/  
  
COPY ./overlay/ /  
  
VOLUME /etc/letsencrypt  

