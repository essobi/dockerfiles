FROM mesoform/alpine-autopilot-base:onbuild-0.4.5  
MAINTAINER dperezsan <dan@mesoform.com>  
LABEL description="Concierge maintained Logstash for Mesoform"  
LABEL com.mesoform.baseimage="False"  
LABEL com.joyent.autopilotpattern="True"  
LABEL com.mesoform.builddate="2017-06-20T10:16:38Z"  
LABEL com.mesoform.baseimage.ver="mesoform/alpine-autopilot-
base:onbuild-0.4.5"  
LABEL com.docker.img.ver="mesoform/logstash:concierge-0.1.16"  
  
# Set some environment variables  
ENV DOCKER_IMG_VER="mesoform/logstash:concierge-0.1.16"  
ENV DNS_DOMAIN="logstash.dockerlx.oaas.mesoform.com"  
ENV CONSUL_AGENT=True  
ENV LOGSTASH_VERSION="logstash-5.4.0"  
ENV PKG="logstash-5.4.0.tar.gz"  
ENV PKG_SHA1="8ee6b30fb2bd6ab9136f907e5f75224dc17e1ed6"  
# set some build variables  
ARG APK_FLAGS_COMMON="-q"  
ARG APK_FLAGS_PERSISTANT="${APK_FLAGS_COMMON} --clean-protected --no-cache"  
# add packages needed for Logstash  
RUN apk update \  
&& apk add ${APK_FLAGS_PERSISTANT} \  
openjdk8 \  
jq \  
nodejs \  
logrotate \  
netcat-openbsd \  
&& rm -rf /var/cache/apk/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
  
# Pull Logstash production version  
RUN curl -Ls -o /tmp/${PKG} \  
"https://artifacts.elastic.co/downloads/logstash/logstash-5.4.0.tar.gz" \  
&& echo "${PKG_SHA1} /tmp/${PKG}" | sha1sum -c \  
&& tar zxf /tmp/${PKG} \  
&& mv /${LOGSTASH_VERSION} /usr/share/logstash \  
&& rm /tmp/${PKG} \  
&& mkdir -p /etc/logstash \  
&& mkdir -p /var/log/logstash \  
&& ln -sf /bin/containerpilot /usr/local/bin/containerpilot  
  
COPY logstash.conf /etc/logstash/conf.d/logstash.conf  
  
EXPOSE 514 12201 24224  

