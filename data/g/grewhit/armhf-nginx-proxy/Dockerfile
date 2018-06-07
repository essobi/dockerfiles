FROM grewhit/armhf-nginx  
  
LABEL MAINTAINER="Greg White grewhit25@gmail.com"  
  
# Install wget and install/updates certificates  
RUN apk add --no-cache --virtual .run-deps \  
ca-certificates go git bash wget openssl \  
&& update-ca-certificates  
  
# Configure Nginx and apply fix for very long server names  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& sed -i 's/worker_processes 1/worker_processes auto/' /etc/nginx/nginx.conf  
  
# Install Forego  
#ADD https://github.com/jwilder/forego/releases/download/v0.16.1/forego
/usr/local/bin/forego  
ADD https://github.com/djmaze/armhf-forego/releases/download/v0.16.1/forego
/usr/local/bin/forego  
RUN chmod u+x /usr/local/bin/forego  
# Install Forego  
#ENV GOPATH /opt/go  
#ENV PATH $PATH:$GOPATH/bin  
#RUN go get -u github.com/ddollar/forego  
ENV DOCKER_GEN_VERSION 0.7.4  
RUN wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
armhf-$DOCKER_GEN_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-gen-linux-
armhf-$DOCKER_GEN_VERSION.tar.gz \  
&& rm /docker-gen-linux-armhf-$DOCKER_GEN_VERSION.tar.gz  
  
COPY . /app/  
WORKDIR /app/  
  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
VOLUME ["/etc/nginx/certs", "/etc/nginx/dhparam"]  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
CMD ["forego", "start", "-r"]  

