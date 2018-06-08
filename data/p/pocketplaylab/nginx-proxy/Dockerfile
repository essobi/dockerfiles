FROM quay.io/playlab/nginx:1.11.1  
MAINTAINER Sebastian Sasu <sebastian.s@pocketplaylab.com>  
  
# Install wget  
RUN apt-get update \  
&& apt-get install -y -q --no-install-recommends \  
wget \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
# Install Forego  
ADD https://github.com/jwilder/forego/releases/download/v0.16.1/forego
/usr/local/bin/forego  
RUN chmod u+x /usr/local/bin/forego  
  
ENV DOCKER_GEN_VERSION 0.7.3  
RUN wget --no-check-certificate --no-proxy https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
RUN mkdir /usr/src/app  
WORKDIR /usr/src/app  
ADD . /usr/src/app  
  
EXPOSE 80  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
  
CMD ["forego", "start", "-r"]  

