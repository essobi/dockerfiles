FROM kisev/openresty:latest  
  
ARG branch=master  
  
RUN curl -L https://github.com/kisev/personal-website/archive/${branch}.tar.gz
| tar -xz \  
&& mkdir -p /var/www \  
&& mv personal-website-master/* /var/www \  
&& chown -R nginx: /var/www  

