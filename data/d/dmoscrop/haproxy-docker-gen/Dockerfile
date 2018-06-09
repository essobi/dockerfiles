FROM haproxy:1.6.4  
MAINTAINER Doug Moscrop doug.moscrop@gmail.com  
  
WORKDIR /app/  
COPY . /app/  
  
RUN touch /var/run/haproxy.pid  
  
EXPOSE 80  
EXPOSE 9000  
ENV DOCKER_HOST unix:///tmp/docker.sock  
ENV DOCKER_GEN_VERSION 0.7.1  
ADD https://github.com/jwilder/docker-gen/releases/download/0.7.1/docker-gen-
linux-amd64-0.7.1.tar.gz /tmp  
RUN tar -C /usr/local/bin -xvzf /tmp/docker-gen-linux-amd64-0.7.1.tar.gz  
RUN rm /tmp/docker-gen-linux-amd64-0.7.1.tar.gz  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
CMD ["docker-gen", "-config", "/app/docker-gen.cfg"]  

