FROM mesoform/alpine-autopilot-base:onbuild-0.4.5  
MAINTAINER dan <dan@mesoform.com>  
LABEL description="Concierge maintained Elasticsearch stack for Mesoform"  
LABEL com.mesoform.baseimage="False"  
LABEL com.joyent.autopilotpattern="True"  
LABEL com.mesoform.builddate="2017-06-12T10:54:23Z"  
LABEL com.mesoform.baseimage.ver="mesoform/alpine-autopilot-
base:onbuild-0.4.5"  
LABEL com.docker.img.ver="mesoform/elasticsearch:concierge-0.1.6"  
  
# Set some environment variables  
ENV DOCKER_IMG_VER="mesoform/elasticsearch:concierge-0.1.6"  
ENV DNS_DOMAIN="elasticsearch.dockerlx.oaas.mesoform.com"  
ENV CONSUL_AGENT=TRUE  
ENV ELASTICSEARCH_VERSION="elasticsearch-5.4.0"  
ENV PKG="elasticsearch-5.4.0.tar.gz"  
ENV PKG_SHA1="880b115be755a923f25aea810e3386ccb723cc55"  
# Set some build variables  
ARG APK_FLAGS_COMMON="-q"  
ARG APK_FLAGS_PERSISTANT="${APK_FLAGS_COMMON} --clean-protected --no-cache"  
# Add packages needed for Elasticsearch  
RUN apk update \  
&& apk add ${APK_FLAGS_PERSISTANT} \  
openjdk7-jre \  
jq \  
netcat-openbsd \  
&& rm -rf /var/cache/apk/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk  
  
# Pull ES production version  
RUN curl -Ls -o /tmp/${PKG} \  
"https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.4.0.tar.gz"
\  
&& echo "${PKG_SHA1} /tmp/${PKG}" | sha1sum -c \  
&& tar zxf /tmp/${PKG} \  
&& rm /tmp/${PKG} \  
&& mv ${ELASTICSEARCH_VERSION} /usr/share/elasticsearch  
  
# Create and take ownership over required directories  
RUN mkdir -p /usr/share/elasticsearch/data \  
/usr/share/elasticsearch/logs \  
/usr/share/elasticsearch/config/scripts \  
&& adduser -DH -s /sbin/nologin elasticsearch \  
&& chown -R elasticsearch:elasticsearch /usr/share/elasticsearch  
  
#USER elasticsearch  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
  
COPY /etc/elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml  
COPY /bin/manage.sh /usr/local/bin  
  
# Expose the data directory as a volume in case we want to mount these  
# as a --volumes-from target; it's important that this VOLUME comes  
# after the creation of the directory so that we preserve ownership  
VOLUME /usr/share/elasticsearch/data  
  
# We don't need to expose these ports in order for other containers on Triton  
# to reach this container in the default networking environment, but if we  
# leave this here then we get the ports as well-known environment variables  
# for purposes of linking  
EXPOSE 9200 9300  

