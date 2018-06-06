FROM mesoform/alpine-autopilot-base:onbuild-0.4.4  
MAINTAINER dan <dan@mesoform.com>  
LABEL description="Concierge maintained Kibana UI for Mesoform"  
LABEL com.mesoform.baseimage="False"  
LABEL com.joyent.autopilotpattern="True"  
LABEL com.mesoform.builddate="2017-06-07T13:29:07Z"  
LABEL com.mesoform.baseimage.ver="mesoform/alpine-autopilot-
base:onbuild-0.4.4"  
LABEL com.docker.img.ver="mesoform/kibana:concierge-0.1.4"  
  
# Set some environment variables  
ENV DOCKER_IMG_VER="mesoform/kibana:concierge-0.1.4"  
ENV DNS_DOMAIN="kibana.dockerlx.oaas.mesoform.com"  
ENV CONSUL_AGENT=True  
ENV KIBANA_VERSION="kibana-5.4.0-linux-x86_64"  
ENV PKG="kibana-5.4.0-linux-x86_64.tar.gz"  
ENV PKG_SHA1="9f21b2eeb96b5c03b25b7d3c98c85e9ca939a3ff"  
# set some build variables  
ARG APK_FLAGS_COMMON="-q"  
ARG APK_FLAGS_PERSISTANT="${APK_FLAGS_COMMON} --clean-protected --no-cache"  
# add packages needed for Kibana  
RUN apk update \  
&& apk add ${APK_FLAGS_PERSISTANT} \  
jq \  
nodejs \  
netcat-openbsd \  
&& rm -rf /var/cache/apk/* \  
&& curl -Ls -o /tmp/${PKG} \  
"https://artifacts.elastic.co/downloads/kibana/kibana-5.4.0-linux-x86_64.tar.gz"
\  
&& echo "${PKG_SHA1} /tmp/${PKG}" | sha1sum -c \  
&& tar zxf /tmp/${PKG} \  
&& mv /${KIBANA_VERSION} /usr/share/kibana \  
&& rm /tmp/${PKG} \  
&& rm -rf /usr/share/kibana/node \  
&& mkdir -p /usr/share/kibana/node/bin \  
&& ln -sf /usr/bin/node /usr/share/kibana/node/bin/node  
  
EXPOSE 5601  

