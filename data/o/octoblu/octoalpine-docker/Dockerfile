FROM octoblu/octoalpine:latest  
MAINTAINER Octoblu <docker@octoblu.com>  
  
ENV DOCKER_VERSION 1.12.6  
env DOCKER_MACHINE_VERSION 0.9.0  
RUN curl -fsSLO
"https://github.com/docker/machine/releases/download/v$DOCKER_MACHINE_VERSION/docker-
machine-Linux-x86_64" \  
&& mv docker-machine-Linux-x86_64 /usr/local/bin/docker-machine \  
&& chmod +x /usr/local/bin/docker-machine  
  
RUN curl -fsSLO
"https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz" \  
&& tar --strip-components=1 -xvzf "docker-$DOCKER_VERSION.tgz" -C
/usr/local/bin \  
&& chmod +x /usr/local/bin/docker \  
&& rm "docker-$DOCKER_VERSION.tgz"  
  
RUN curl -o /usr/local/bin/docker-swarm-diff -fsSL
https://github.com/octoblu/docker-swarm-
diff/releases/download/docker1.12-v1.0.3/docker-swarm-diff-linux-amd64 \  
&& chmod +x /usr/local/bin/docker-swarm-diff \  
&& ln -nsf /usr/local/bin/docker-swarm-diff /usr/local/bin/dsd  

