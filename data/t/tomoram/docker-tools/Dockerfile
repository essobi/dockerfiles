FROM ubuntu  
  
RUN apt-get update \  
&& apt-get install -y bash \  
&& apt-get install -y wget \  
&& apt-get install -y curl \  
&& apt-get install -y jq  
  
# Install docker client  
RUN mkdir /install \  
&& cd /install \  
&& wget \--no-check-certificate
https://get.docker.com/builds/Linux/x86_64/docker-1.12.2.tgz \  
&& tar xvzf docker-1.12.2.tgz \  
&& cp docker/docker /usr/local/bin \  
&& rm -rf /install  
  
# Install docker machine  
RUN curl -L
"https://github.com/docker/machine/releases/download/v0.8.2/docker-
machine-$(uname -s)-$(uname -m)" >/usr/local/bin/docker-machine \  
&& chmod +x /usr/local/bin/docker-machine  
  
# Install docker compose  
RUN curl -L "https://github.com/docker/compose/releases/download/1.8.1/docker-
compose-$(uname -s)-$(uname -m)" >/usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  
  
ADD scripts/json-to-docker-machine /usr/local/bin/  
RUN chmod a+x /usr/local/bin/json-to-docker-machine  
  
ADD scripts/env-to-docker-machine /usr/local/bin/  
RUN chmod a+x /usr/local/bin/env-to-docker-machine  

