FROM nginx:latest  
#FROM nginx:1.9.9  
MAINTAINER Jason Wilder mail@jasonwilder.com  
  
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
WORKDIR /tmp/  
RUN wget -O forego.tgz https://bin.equinox.io/c/ekMN3bCZFUn/forego-stable-
linux-amd64.tgz  
RUN gunzip /tmp/forego.tgz && tar -xvf forego.tar  
RUN mv forego /usr/local/bin && chmod u+x /usr/local/bin/forego  
RUN rm forego.tar  
  
ENV DOCKER_GEN_VERSION 0.7.3  
RUN wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz  
RUN tar -C /usr/local/bin -xvzf /tmp/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz  
RUN rm docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
COPY . /app/  
WORKDIR /app/  
  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
VOLUME ["/etc/nginx/certs"]  
  
RUN ["chmod", "755", "/app"]  
RUN ["chmod", "755", "/app/docker-entrypoint.sh"]  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
  
CMD ["forego", "start", "-r"]

