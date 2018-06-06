FROM nginx:1.9.15  
# Install wget and install/updates certificates  
RUN apt-get update \  
&& apt-get install -y -q --no-install-recommends \  
ca-certificates \  
wget \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
# Configure Nginx and apply fix for very long server names  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& sed -i 's/^http {/&\n server_names_hash_bucket_size 128;/g'
/etc/nginx/nginx.conf \  
&& sed -i 's/^http {/&\n limit_conn_zone $binary_remote_addr zone=addr:10m;/g'
/etc/nginx/nginx.conf \  
# Increased the number of worker_processes to 4  
&& sed -i 's/\\(worker_processes\s*\\)[0-9]*;/\14;/' /etc/nginx/nginx.conf \  
# Increased the number of worker_connections from any number to 10240  
&& sed -i 's/\\(worker_connections\s*\\)[0-9]*;/\110240;/'
/etc/nginx/nginx.conf  
  
# Install Forego  
ADD https://github.com/jwilder/forego/releases/download/v0.16.1/forego
/usr/local/bin/forego  
RUN chmod u+x /usr/local/bin/forego  
  
ENV DOCKER_GEN_VERSION 0.7.3  
RUN wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
COPY . /app/  
WORKDIR /app/  
  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
VOLUME ["/etc/nginx/certs"]  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
CMD ["forego", "start", "-r"]  

