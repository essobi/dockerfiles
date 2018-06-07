FROM debian:jessie  
RUN apt-get update && apt-get install -y curl  
RUN curl https://get.docker.io/builds/Linux/x86_64/docker-latest -o
/usr/local/bin/docker && chmod +x /usr/local/bin/docker  
RUN curl -L https://github.com/docker/fig/releases/download/1.0.1/fig-
Linux-x86_64 > /usr/local/bin/fig && chmod +x /usr/local/bin/fig  
ENV DOCKER_HOST unix:///docker.sock  
ENTRYPOINT ["/usr/local/bin/fig"]  

