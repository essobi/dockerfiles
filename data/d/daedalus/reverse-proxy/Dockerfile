  
############################################################  
# Dockerfile to build reverse proxy container images  
# Based on the jwilder/nginx-proxy container image. At the moment,  
# it is identical, but I would like to be able to change config if  
# I need to. If you would like to use a properly maintained version  
# please use the version found here https://github.com/jwilder/nginx-proxy  
############################################################  
# Set the base image to nginx:1.9.2  
  
FROM nginx:1.9.2  
MAINTAINER Jonathan Temlett jono@daedalus.co.za  
  
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
/etc/nginx/nginx.conf  
  
# Install Forego  
RUN wget -P /usr/local/bin
https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-
amd64/forego \  
&& chmod u+x /usr/local/bin/forego  
  
ENV DOCKER_GEN_VERSION 0.4.2  
  
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

