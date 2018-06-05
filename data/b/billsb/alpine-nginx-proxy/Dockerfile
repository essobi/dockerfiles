FROM nginx:alpine  
  
ENV HOME /usr/src/app  
  
# Configure Nginx and apply fix for very long server names  
RUN sed -i 's/^http {/&\n server_names_hash_bucket_size 128;/g'
/etc/nginx/nginx.conf  
  
RUN apk --no-cache add bash curl  
  
ENV FOREGO_VERSION v0.16.1  
ADD https://github.com/jwilder/forego/releases/download/$FOREGO_VERSION/forego
/usr/local/bin/forego  
RUN chmod u+x /usr/local/bin/forego  
  
ENV DOCKER_GEN_VERSION 0.7.3  
RUN curl -sL\  
https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-alpine-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz |\  
tar -C /usr/local/bin -xvzf - && chown root:root /usr/local/bin/docker-gen  
  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
VOLUME ["/etc/nginx/certs"]  
  
COPY . $HOME  
WORKDIR $HOME  
  
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]  
CMD ["forego", "start", "-r"]  

