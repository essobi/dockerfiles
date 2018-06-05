FROM ubuntu:14.04.2  
MAINTAINER Patrick Carey patrick@rehabstudio.com  
  
# Install wget and install/updates certificates  
RUN apt-get update \  
&& apt-get install -y -q --no-install-recommends \  
ca-certificates \  
wget \  
dnsmasq \  
supervisor \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
# Install docker-gen  
ENV DOCKER_GEN_VERSION 0.3.7  
RUN wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
COPY . /app/  
ADD supervisord.conf /etc/supervisor/conf.d/dnsmasq.conf  
WORKDIR /app/  
  
EXPOSE 53/udp  
  
ENV DOCKER_HOST unix:///var/run/docker.sock  
  
CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]  

