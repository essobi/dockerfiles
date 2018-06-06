FROM python:2.7.13-slim  
MAINTAINER Andrey N. Petrov <andreynpetrov@gmail.com>  
LABEL description="celery"  
  
RUN groupadd user && useradd --create-home --home-dir /home/user -g user user  
  
COPY requirements.txt /home/user/requirements.txt  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget rsyslog && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
# Install dumb-init and rsyslog  
&& wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64.deb \  
&& dpkg -i dumb-init_1.2.0_amd64.deb \  
&& apt-get purge -y --auto-remove ca-certificates wget \  
&& ln -s /dev/console /dev/xconsole  
  
RUN set -x \  
&& mkdir /home/user/workers \  
&& apt-get update \  
&& apt-get -y install \  
build-essential \  
libffi-dev \  
libssl-dev \  
&& pip install -r /home/user/requirements.txt \  
&& apt-get purge -y --auto-remove \  
build-essential \  
libffi-dev \  
libssl-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
  
WORKDIR /home/user/workers  
  
ENV CELERY_BROKER_USERNAME admin  
ENV CELERY_BROKER_PASSWORD admin  
ENV CELERY_BROKER_VHOST demo  
ENV CELERY_KEYFILE /etc/tls/client_key.pem  
ENV CELERY_CERTFILE /etc/tls/client_certificate.pem  
ENV CELERY_CA_CERTS /etc/tls/ca_certificate.pem  
  
COPY files/docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
  
CMD ["/docker-entrypoint.sh"]  

