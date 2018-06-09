FROM debian:8  
MAINTAINER "Sascha Marcel Schmidt" <docker@saschaschmidt.net>  
  
RUN apt-get update && apt-get install -y curl && rm -r /var/lib/apt/lists/*  
RUN curl -fL https://get.docker.com/ | sh && rm -r /var/lib/apt/lists/*  
RUN curl -fL https://github.com/docker/compose/releases/download/1.7.1/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && chmod +x
/usr/local/bin/docker-compose  
  
RUN useradd gitlab_ci_runner  
RUN groupadd -g 1001 dockerhost && gpasswd -a gitlab_ci_runner dockerhost  

