FROM funkygibbon/nginx:latest  
MAINTAINER Ray Walker <hello@raywalker.it>  
  
# Install wget and install/updates certificates  
RUN apt-get update \  
&& apt-get install -y -q --no-install-recommends \  
ca-certificates \  
wget \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
ENV DOCKER_GEN_VERSION 0.7.3  
RUN wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
COPY . /app/  
WORKDIR /app/  
  
RUN rm -f /etc/nginx/sites-enabled/* \  
&& cp -Rf etc/* /etc  
  
RUN chmod +x /etc/service/dockergen/run  
  
# Update default nginx.conf  
# - apply fix for very long server names  
# - delete access_log to allow for per-virtual host customisation in
nginx.tmpl  
RUN sed -i 's/^http {/&\n server_names_hash_bucket_size 128;/g; /access_log/d'
/etc/nginx/nginx.conf  
  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
VOLUME ["/etc/nginx/certs"]  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
CMD ["/sbin/my_init"]  

