FROM podbox/debian  
  
RUN (curl -L http://nginx.org/keys/nginx_signing.key | apt-key add -) \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >
/etc/apt/sources.list.d/nginx.list  
  
RUN apt-get update \  
&& apt-get install -yq nginx  
  
EXPOSE 80 443  
CMD service nginx start && tail -f /var/log/nginx/access.log

