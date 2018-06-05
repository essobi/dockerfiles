FROM debian:stretch-slim  
  
ARG SENSU_VERSION=1.4.2-3  
ARG DOCKERIZE_VERSION=0.6.1  
RUN groupadd -r sensu && useradd -r -g sensu sensu \  
&& apt-get update && apt-get install -y wget ca-certificates gnupg --no-
install-recommends && rm -rf /var/lib/apt/lists/* \  
&& wget -q http://sensu.global.ssl.fastly.net/apt/pubkey.gpg && apt-key add
pubkey.gpg \  
&& echo "deb http://sensu.global.ssl.fastly.net/apt stretch main" >
/etc/apt/sources.list.d/sensu.list \  
&& apt-get update && apt-get install -y --no-install-recommends
sensu=${SENSU_VERSION} \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget
https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-
linux-amd64-v${DOCKERIZE_VERSION}.tar.gz \  
&& tar -C /usr/local/bin -xvzf dockerize-linux-
amd64-v${DOCKERIZE_VERSION}.tar.gz \  
&& rm dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz  
  
COPY templates /templates  
  
ENV RABBITMQ_HOST=rabbitmq \  
RABBITMQ_PORT=5672 \  
RABBITMQ_USER=guest \  
RABBITMQ_PASSWORD=guest \  
RABBITMQ_VHOST=/ \  
REDIS_HOST=redis \  
REDIS_PORT=6379 \  
API_HOST=sensu-api \  
API_PORT=4567  
RUN chown -R sensu:sensu /etc/sensu  

