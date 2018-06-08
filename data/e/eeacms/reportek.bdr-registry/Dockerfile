FROM python:3.6-slim  
MAINTAINER "EEA: IDM2 C-TEAM" <eea-edw-c-team-alerts@googlegroups.com>  
  
ENV BDR_REG_ROOT=/bdrreg \  
BDR_REG_APP=/bdrreg/bdr-registry \  
BDR_REG_PORT=8080 \  
GOSU_VERSION=1.7  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
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
&& gosu nobody true  
  
RUN useradd --system -U -u 500 bdrreg \  
&& mkdir -p $BDR_REG_ROOT/logs $BDR_REG_ROOT/static \  
&& chown -R bdrreg:bdrreg $BDR_REG_ROOT  
  
VOLUME ["$BDR_REG_ROOT/static"]  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends curl \  
netcat \  
sudo \  
python-setuptools \  
python-dev \  
build-essential \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
libbz2-dev \  
libldap2-dev \  
libsasl2-dev  
  
COPY . $BDR_REG_APP  
WORKDIR $BDR_REG_APP  
  
RUN pip install -r requirements.txt \  
&& chown -R 500:500 $BDR_REG_ROOT  
  
ENTRYPOINT ["./docker-setup.sh"]  
CMD ["run"]  

