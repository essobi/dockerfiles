FROM suckowbiz/base  
  
LABEL maintainer="Tobias Suckow <tobias@suckow.biz>"  
RUN apt-get install --quiet --quiet --yes --no-install-recommends \  
nginx  
  
RUN \  
# Increase timeout (will not affect all browsers) to have larger interval
allowing more actions.  
sed --in-place "s/keepalive_timeout\s*65/keepalive_timeout 2/g"
/etc/nginx/nginx.conf \  
# Setting client_max_body_size to 0 disables checking of client request body
size.  
&& sed --in-place "s/keepalive_timeout 2/keepalive_timeout
2;\n\tclient_max_body_size 0/g" /etc/nginx/nginx.conf \  
# NGINX must not run as daemon to avoid container stops right after start  
&& echo "daemon off;" >> /etc/nginx/nginx.conf  
  
COPY context /  
ENV ENTRYPOINT_AS_ROOT=yes  
ENTRYPOINT ["/entrypoint.sh", "/start.sh"]  
CMD ["/etc/init.d/nginx", "start"]  

