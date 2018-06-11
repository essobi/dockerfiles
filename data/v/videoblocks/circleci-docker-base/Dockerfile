FROM node:6.10  
RUN set -x \  
&& VER="17.03.0-ce" ; curl -L -o /tmp/docker-$VER.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$VER.tgz \  
&& tar -xz -C /tmp -f /tmp/docker-$VER.tgz \  
&& mv /tmp/docker/* /usr/local/bin/  
  
RUN curl -L
"https://github.com/docker/compose/releases/download/1.12.0/docker-
compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  

