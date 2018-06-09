FROM toune/docker-nginx  
  
# MAINTAINER Jason Wilder mail@jasonwilder.com  
# MAINTAINER Pooya Parsa <pooya@pi0.ir>  
# Install packages  
RUN apk update  
RUN apk add ca-certificates wget supervisor  
  
# Setup ENV & Startup scripts  
ENV DOCKER_HOST unix:///tmp/docker.sock  
ENV DOCKER_GEN_VERSION 0.7.3  
VOLUME ["/etc/nginx/certs"]  
WORKDIR /app/  
ENTRYPOINT ["/app/entrypoint"]  
CMD ["supervisord", "-c", "/app/supervisord.conf"]  
  
# Install docker-gen  
RUN wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& rm docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
# Default domain  
RUN echo "Domain does not exist." > /usr/share/nginx/html/index.html  
  
COPY /app/nginx.conf /etc/nginx/nginx.conf  
COPY app /app/  

