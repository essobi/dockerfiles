FROM newsmedianl/python-node-yarn:latest  
  
RUN \  
echo "Installing nginx and supervisor" && \  
curl -s https://nginx.org/keys/nginx_signing.key | apt-key add \- && \  
echo "deb http://nginx.org/packages/mainline/debian/ stretch nginx" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y nginx nginx-module-geoip supervisor  

