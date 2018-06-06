FROM alpine:3.6  
LABEL maintainer="Gareth Brown <gareth@mesoform.com>"  
LABEL description="Mesoform base Alpine Linux image which uses the autopilot
pattern for self-orchestration"  
LABEL com.mesoform.baseimage="True"  
LABEL com.joyent.autopilotpattern="True"  
LABEL com.mesoform.builddate="2018-03-14T16:05:57Z"  
LABEL com.mesoform.baseimage.ver="alpine:3.6"  
LABEL com.docker.img.ver="mesoform/concierge-alpine-base-image:0.1.20"  
  
#################################  
### General environment setup ###  
# set Dockerfile build-time arguements  
ARG APK_FLAGS_COMMON="-q"  
ARG APK_FLAGS_PERSISTANT="${APK_FLAGS_COMMON} --clean-protected --no-cache"  
ARG APK_FLAGS_DEV="${APK_FLAGS_COMMON} --no-cache"  
# set container environment variables  
ENV TERM=xterm  
ENV CONTAINERPILOT_VERSION=3.6.0  
ENV CONTAINERPILOT_CHECKSUM=1248784ff475e6fda69ebf7a2136adbfb902f74b  
ENV CONTAINERPILOT=/etc/containerpilot.json5  
ENV HOSTMETADATA=concierge-alpine-base-image.dockerlx  
ENV ZBX_VERSION=3.2.6  
ENV ZBX_SOURCES=svn://svn.zabbix.com/tags/3.2.6/  
ENV LOG_FORMAT=text  
ENV LOG_LEVEL=INFO  
ENV DOCKER_IMG_VER="mesoform/concierge-alpine-base-image:0.1.20"  
ENV CONSUL_AGENT=TRUE  
ENV CONSUL_VERSION=1.0.0  
ENV
CONSUL_CHECKSUM=585782e1fb25a2096e1776e2da206866b1d9e1f10b71317e682e03125f22f479  
ENV CONSUL_TEMPLATE_VERSION=0.19.4  
ENV
CONSUL_TEMPLATE_CHECKSUM=5f70a7fb626ea8c332487c491924e0a2d594637de709e5b430ecffc83088abc0  
ENV
CONCIERGE_COURIER_URL=https://raw.githubusercontent.com/mesoform/concierge_courier/master/src/concierge_courier/concierge_courier.py  
ENV CONCIERGE_COURIER_LOC=/usr/local/bin/concierge_courier.py  
ENV PIS_FILE=https://raw.githubusercontent.com/mesoform/Container-Platform-
Scripts/master/src/platform_integration/platform_integration.sh  
ENV PIS_LOC=/usr/local/bin/platform_integration.sh  
  
# Install some basic operating utilities  
RUN apk update && \  
apk add ${APK_FLAGS_PERSISTANT} \  
pcre pcre-dev libpcre16 libpcre32 libpcrecpp \  
supervisor \  
curl \  
bash \  
ca-certificates \  
coreutils \  
py-requests \  
libcap \  
libssl1.0 && \  
rm -rf /var/cache/apk/*  
  
##############################  
### Install ContainerPilot ###  
RUN curl -Lso /tmp/containerpilot.tar.gz \  
"https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/containerpilot-${CONTAINERPILOT_VERSION}.tar.gz"
&& \  
echo "${CONTAINERPILOT_CHECKSUM} /tmp/containerpilot.tar.gz" | sha1sum -c && \  
tar zxf /tmp/containerpilot.tar.gz -C /usr/local/bin && \  
rm /tmp/containerpilot.tar.gz  
  
######################  
### Install Consul ###  
# Releases at https://releases.hashicorp.com/consul  
RUN export archive=consul_${CONSUL_VERSION}_linux_amd64.zip && \  
curl -Lso /tmp/${archive}
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/${archive} && \  
echo "${CONSUL_CHECKSUM} /tmp/${archive}" | sha256sum -c && \  
cd /usr/local/bin && \  
unzip /tmp/${archive} && \  
chmod +x /usr/local/bin/consul && \  
rm /tmp/${archive}  
  
# Create empty directories for Consul config and data  
RUN mkdir -p /etc/coprocesses/consul && \  
mkdir -p /var/lib/consul  
  
###############################  
### Install Consul template ###  
# Releases at https://releases.hashicorp.com/consul-template/  
RUN curl --retry 7 --fail -Lso /tmp/consul-template.zip \  
"https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" && \  
echo "${CONSUL_TEMPLATE_CHECKSUM} /tmp/consul-template.zip" | sha256sum -c &&
\  
unzip /tmp/consul-template.zip -d /usr/local/bin && \  
rm /tmp/consul-template.zip  
  
############################  
### Install Zabbix Agent ###  
# https://hub.docker.com/r/zabbix/zabbix-agent/~/dockerfile/  
RUN addgroup zabbix && \  
adduser -S \  
-D -G zabbix \  
-h /var/lib/zabbix/ \  
zabbix && \  
mkdir -p /etc/zabbix && \  
mkdir -p /etc/coprocesses/zabbix/zabbix_agentd.d && \  
mkdir -p /var/lib/zabbix/enc && \  
mkdir -p /var/lib/zabbix/modules && \  
chown --quiet -R zabbix:root /var/lib/zabbix  
  
# For now, just add Zabbix Sender from the zabbix-utils package  
RUN apk update && \  
apk add zabbix-utils && \  
apk add ${APK_FLAGS_DEV} \--virtual build-dependencies \  
alpine-sdk \  
automake \  
autoconf \  
openssl-dev \  
zabbix-utils \  
subversion && \  
cd /tmp/ && \  
svn --quiet export ${ZBX_SOURCES} zabbix-${ZBX_VERSION} 1>/dev/null && \  
cd /tmp/zabbix-${ZBX_VERSION} && \  
zabbix_revision=$(svn info ${ZBX_SOURCES} |grep "Last Changed Rev"|awk '{print
$4;}') && \  
sed -i "s/{ZABBIX_REVISION}/$zabbix_revision/g" include/version.h && \  
./bootstrap.sh 1>/dev/null && \  
./configure \  
\--prefix=/usr \  
\--silent \  
\--sysconfdir=/etc/coprocesses/zabbix/ \  
\--libdir=/usr/lib/zabbix \  
\--datadir=/usr/lib \  
\--enable-agent \  
\--enable-ipv6 \  
\--with-openssl && \  
make -j"$(nproc)" -s 1>/dev/null && \  
cp src/zabbix_agent/zabbix_agentd /usr/sbin/zabbix_agentd && \  
cp conf/zabbix_agentd.conf /etc/zabbix/ && \  
chown --quiet -R zabbix:root /etc/zabbix && \  
cd /tmp/ && \  
rm -rf /tmp/zabbix-${ZBX_VERSION}/ && \  
apk del --purge \  
build-dependencies && \  
rm -rf /var/cache/apk/*  
  
#############################  
## Fetch Concierge Courier ##  
RUN curl --retry 7 --fail -Lso ${CONCIERGE_COURIER_LOC}
${CONCIERGE_COURIER_URL} && \  
chmod +x ${CONCIERGE_COURIER_LOC}  
  
######################################  
## Fetch Platform Integration Setup ##  
RUN curl --retry 7 --fail -Lso ${PIS_LOC} ${PIS_FILE} && \  
chmod +x ${PIS_LOC}  
  
# copy some files so that the base image can be tested  
COPY metrics.json /tmp/  
COPY etc /etc/  
COPY bin /usr/local/bin/  
RUN chmod -R +x /usr/local/bin/  
  
# open zabbix port  
EXPOSE 10050/TCP  
  
# This may conflict with main application when agent is setup as a coprocess  
#WORKDIR /var/lib/zabbix  
VOLUME ["/etc/coprocesses/zabbix/zabbix_agentd.d", "/var/lib/zabbix/enc",
"/var/lib/zabbix/modules"]  
  
ENTRYPOINT ["/usr/local/bin/containerpilot"]  
#ENTRYPOINT ["/bin/sh"]  
#CMD ${APP_CMD:-/bin/bash}  
ONBUILD RUN apk update && apk upgrade ${APK_FLAGS_PERSISTANT} \--latest  
ONBUILD COPY etc /etc/  
ONBUILD COPY bin /usr/local/bin/

