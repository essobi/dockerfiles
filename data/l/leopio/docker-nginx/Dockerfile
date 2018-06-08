FROM debian:wheezy  
  
ENV VERSION 1  
RUN apt-get update \  
&& apt-get install -y wget ca-certificates nginx \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64.deb  
RUN dpkg -i dumb-init_*.deb  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN rm -rf /etc/nginx/conf.d/*  
RUN rm -rf /srv/www/*  
  
RUN useradd -ms /bin/bash nginx  
  
ADD nginx.conf /etc/nginx/  
ADD default.conf /etc/nginx/conf.d/default.conf  
ADD index.html /srv/www/index.html  
ADD default.conf /etc/nginx/sites-available/  
  
RUN rm /etc/nginx/sites-enabled/default  
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default  
  
VOLUME ["/etc/nginx"]  
VOLUME ["/srv/www"]  
  
EXPOSE 80  
EXPOSE 443  
CMD ["dumb-init","nginx", "-g", "daemon off;"]  

