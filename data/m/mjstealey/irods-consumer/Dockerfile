FROM debian:jessie  
MAINTAINER Michael J. Stealey <michael.j.stealey@gmail.com>  
  
RUN set -ex; \  
if ! command -v gpg > /dev/null; then \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
gnupg \  
dirmngr \  
; \  
rm -rf /var/lib/apt/lists/*; \  
fi  
  
# set user/group IDs for irods account  
RUN groupadd -r irods --gid=998 \  
&& useradd -r -g irods -d /var/lib/irods --uid=998 irods  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.10  
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
&& rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
# install iRODS v4.2.1  
RUN apt-get update && apt-get install -y \  
wget \  
libxml2 \  
apt-transport-https \  
sudo \  
jq \  
&& wget -qO - https://packages.irods.org/irods-signing-key.asc | apt-key add -
\  
&& echo "deb [arch=amd64] https://packages.irods.org/apt/ trusty main" \  
> /etc/apt/sources.list.d/renci-irods.list \  
&& apt-get update && apt-get install -y \  
irods-externals-avro1.7.7-0 \  
irods-externals-boost1.60.0-0 \  
irods-externals-clang-runtime3.8-0 \  
irods-externals-jansson2.7-0 \  
irods-externals-libarchive3.1.2-0 \  
irods-externals-zeromq4-14.1.3-0 \  
irods-icommands=4.2.1 \  
irods-runtime=4.2.1 \  
irods-server=4.2.1  
  
# default iRODS env  
ENV IRODS_SERVICE_ACCOUNT_NAME=irods  
ENV IRODS_SERVICE_ACCOUNT_GROUP=irods  
# 1. provider, 2. consumer  
ENV IRODS_SERVER_ROLE=2  
ENV IRODS_PROVIDER_ZONE_NAME=tempZone  
ENV IRODS_PROVIDER_HOST_NAME=provider  
ENV IRODS_PORT=1247  
ENV IRODS_PORT_RANGE_BEGIN=20000  
ENV IRODS_PORT_RANGE_END=20199  
ENV IRODS_CONTROL_PLANE_PORT=1248  
ENV IRODS_SCHEMA_VALIDATION=file:///var/lib/irods/configuration_schemas  
ENV IRODS_SERVER_ADMINISTRATOR_USER_NAME=rods  
ENV IRODS_SERVER_ZONE_KEY=TEMPORARY_zone_key  
ENV IRODS_SERVER_NEGOTIATION_KEY=TEMPORARY_32byte_negotiation_key  
ENV IRODS_CONTROL_PLANE_KEY=TEMPORARY__32byte_ctrl_plane_key  
ENV IRODS_SERVER_ADMINISTRATOR_PASSWORD=rods  
ENV IRODS_VAULT_DIRECTORY=/var/lib/irods/iRODS/Vault  
# UID / GID settings  
ENV UID_IRODS=998  
ENV GID_IRODS=998  
# create irods.tar.gz  
RUN cd /var/lib/irods \  
&& tar -czvf /irods.tar.gz . \  
&& cd /  
  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
VOLUME /var/lib/irods /etc/irods  
  
EXPOSE $IRODS_PORT $IRODS_CONTROL_PLANE_PORT
$IRODS_PORT_RANGE_BEGIN-$IRODS_PORT_RANGE_END  
ENTRYPOINT ["/docker-entrypoint.sh"]  
WORKDIR "/var/lib/irods"  
  
CMD ["-i", "run_irods"]

