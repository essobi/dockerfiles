FROM quay.io/letsencrypt/letsencrypt:latest  
  
# Install wget and install/updates certificates  
RUN apt-get update \  
&& apt-get install -y -q --no-install-recommends \  
ca-certificates \  
wget \  
nano \  
curl \  
jq \  
docker.io \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
# install docker-gen  
ENV DOCKER_GEN_VERSION 0.7.3  
WORKDIR /tmp  
RUN wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& rm docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
# Install Forego  
ADD https://github.com/jwilder/forego/releases/download/v0.16.1/forego
/usr/local/bin/forego  
RUN chmod u+x /usr/local/bin/forego  
  
# install app  
COPY app /app  
RUN mkdir -p /app/run  
RUN chmod +x /app/*.sh  
  
WORKDIR /app/  
  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/certbot/venv/bin  
  
ENTRYPOINT ["/app/entrypoint.sh"]  
  
CMD ["forego", "start", "-r"]  

