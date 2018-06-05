FROM benhall/nginx-proxy:1.11.1-sticky  
MAINTAINER Daniel Haus <daniel.haus@businesstools.de>  
# VERSION 0.4.0  
RUN { \  
echo 'server_tokens off;'; \  
echo 'client_max_body_size 1g;'; \  
} > /etc/nginx/conf.d/my_proxy.conf  

