FROM jwilder/nginx-proxy  
  
MAINTAINER Joeri Verdeyen <joeriv@yappa.be>  
  
RUN { \  
echo 'server_tokens off;'; \  
echo 'client_max_body_size 200m;'; \  
} > /etc/nginx/conf.d/my_proxy.conf

