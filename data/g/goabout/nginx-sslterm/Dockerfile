FROM goabout/nginx  
  
MAINTAINER Go About <tech@goabout.com>  
  
# Install packages  
RUN apt-get update -q && \  
apt-get install -yq --no-install-recommends \  
ca-certificates \  
wget \  
&& \  
apt-get clean && \  
rm -r /var/lib/apt/lists/*  
  
# Install Forego  
RUN wget -P /usr/local/bin
https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-
amd64/forego && \  
chmod u+x /usr/local/bin/forego  
  
# Install docker-gen  
ENV DOCKER_GEN_VERSION 0.4.2  
RUN wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz && \  
tar -C /usr/local/bin -xvzf docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz
&& \  
rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
# Copy files  
COPY ssl_certificate.pem ssl_certificate_key.pem ssl_trusted_certificate.pem
/templates/etc/nginx/  
COPY Procfile docker-gen.cfg nginx.conf.tmpl /templates/work/  
  
WORKDIR /work  
CMD ["forego", "start", "-r"]  

