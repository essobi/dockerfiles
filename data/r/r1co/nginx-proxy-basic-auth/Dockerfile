FROM ubuntu:latest  
  
# Install wget and install/updates certificates  
RUN apt-get update \  
&& apt-get install -y -q --no-install-recommends \  
ca-certificates \  
wget \  
nano \  
curl \  
jq \  
apache2-utils \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
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
  
COPY app /app  
WORKDIR /app/  
RUN chmod +x *  
  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
ENTRYPOINT ["/app/entrypoint.sh"]  
CMD ["forego", "start", "-r"]

