FROM nginx:1.7  
MAINTAINER Jessica Liu  
  
# Install htpasswd utility and curl  
RUN apt-get update \  
&& apt-get install -y curl apache2-utils zip vim \  
&& rm -rf /etc/nginx/conf.d/* \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Kibana  
ENV KIBANA_VERSION 4.0.3  
RUN mkdir -p /var/www \  
&& curl -s
https://download.elasticsearch.org/kibana/kibana/kibana-$KIBANA_VERSION-
linux-x64.tar.gz \  
| tar --transform "s/^kibana-$KIBANA_VERSION/kibana/" -xvz -C /var/www \  
&& mv /var/www/kibana-linux-x64 /var/www/kibana  
  
# Copy Nginx config  
COPY config/nginx.conf /etc/nginx/nginx.conf  
COPY config/kibana.conf /etc/nginx/conf.d/kibana.conf  
  
# Add default credentials  
RUN htpasswd -cb /etc/nginx/.htpasswd kibana "docker"  
  
ENV PATH /var/www/kibana/bin:$PATH  
COPY scripts/docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
EXPOSE 5601  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

