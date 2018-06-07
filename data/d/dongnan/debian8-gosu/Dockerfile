# vim:set ft=dockerfile:  
FROM debian:jessie  
MAINTAINER DongNan <dongyh@126.com>  
  
ENV GOSU_VERSION=1.7  
RUN \  
# add gosu for easy step-down from root  
set -x \  
&& DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
ca-certificates curl \  
#&& rm -rf /var/lib/apt/lists/* \  
#&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& curl -fSL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" -o /usr/local/bin/gosu \  
#&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& curl -fSL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" -o /usr/local/bin/gosu.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
# install "pwgen" for randomizing passwords  
# install "apt-transport-https" for Percona's repo (switched to https-only)  
RUN \  
#DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
apt-transport-https ca-certificates \  
pwgen \  
&& apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys \  
# pub 1024D/CD2EFD2A 2009-12-15  
# Key fingerprint = 430B DF5C 56E7 C94E 848E E60C 1C4C BDCD CD2E FD2A  
# uid Percona MySQL Development Team <mysql-dev@percona.com>  
# sub 2048g/2D607DAF 2009-12-15  
430BDF5C56E7C94E848EE60C1C4CBDCDCD2EFD2A \  
# pub 4096R/8507EFA5 2016-06-30  
# Key fingerprint = 4D1B B29D 63D9 8E42 2B21 13B1 9334 A25F 8507 EFA5  
# uid Percona MySQL Development Team (Packaging key) <mysql-dev@percona.com>  
# sub 4096R/4CAC6D72 2016-06-30  
4D1BB29D63D98E422B2113B19334A25F8507EFA5  

