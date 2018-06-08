# logstash  
FROM phusion/baseimage  
MAINTAINER paladintyrion <paladintyrion@gmail.com>  
  
###############################################################################  
# GROUP && USER  
###############################################################################  
  
ENV LOGSTASH_HOME /opt/logstash  
# ensure logstash user exists  
ENV LOGSTASH_GID 442  
ENV LOGSTASH_UID 442  
RUN groupadd -r logstash -g ${LOGSTASH_GID} \  
&& useradd -r -s /usr/sbin/nologin -d ${LOGSTASH_HOME} -c "Logstash service
user" -u ${LOGSTASH_UID} -g logstash logstash  
  
###############################################################################  
# GOSU && TIMEZONE && JDK8  
###############################################################################  
  
ENV GOSU_VERSION 1.10  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get install -yq --no-install-recommends tzdata cron \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& apt-get install -qqy --no-install-recommends ca-certificates wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture | awk -F- '{ print $NF }').asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get update -qq \  
&& apt-get install -qqy openjdk-8-jdk \  
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& apt-get clean \  
&& rm -fr /tmp/* \  
&& set +x  
  
###############################################################################  
# INSTALL LOGSTASH  
###############################################################################  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LOGSTASH_PATH $LOGSTASH_HOME/bin  
ENV PATH $LOGSTASH_PATH:$PATH  
  
RUN mkdir -p $LOGSTASH_HOME \  
&& mkdir -p /var/log/logstash /etc/logstash/conf.d /var/lib/logstash
/tmp/logstash \  
&& chown -R logstash:logstash ${LOGSTASH_HOME} /var/log/logstash /etc/logstash
/var/lib/logstash /tmp/logstash \  
&& mkdir -p /etc/logrotate.d  
  
ENV VERSION 6.0.0  
ENV URL "https://artifacts.elastic.co/downloads/logstash"  
ENV TARBALL "$URL/logstash-${VERSION}.tar.gz"  
ENV TARBALL_ASC "$URL/logstash-${VERSION}.tar.gz.asc"  
ENV TARBALL_SHA
"0b35057a7308152de43927f06fbe0198c5c3135d9fa0dec1b48feeea084ecc04b3f6852c9c0239f6f854f5ea0a7a2cd33432a9faddbd6b523f2de336c8b21aaf
logstash.tar.gz"  
ENV GPG_KEY "46095ACC8548582C1A2699A9D27D666CD88E42B4"  
  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get install -yq --no-install-recommends gnupg openssl tar \  
&& cd /tmp \  
&& wget --progress=bar:force -O logstash.tar.gz "$TARBALL"; \  
if [ "$TARBALL_SHA" ]; then \  
echo "$TARBALL_SHA" | sha512sum -c -; \  
fi; \  
\  
if [ "$TARBALL_ASC" ]; then \  
wget --progress=bar:force -O logstash.tar.gz.asc "$TARBALL_ASC"; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY"; \  
gpg --batch --verify logstash.tar.gz.asc logstash.tar.gz; \  
rm -r "$GNUPGHOME" logstash.tar.gz.asc; \  
fi; \  
\  
mkdir -p "$LOGSTASH_HOME"; \  
tar -xzf logstash.tar.gz --strip-components=1 -C "$LOGSTASH_HOME"; \  
rm -f logstash.tar.gz; \  
logstash --version; \  
set +x  
  
RUN apt-get autoremove \  
&& apt-get autoclean  
  
COPY ./config/logstash/logstash-init /etc/init.d/logstash  
RUN sed -i -e 's#^LS_HOME=$#LS_HOME='$LOGSTASH_HOME'#' /etc/init.d/logstash \  
&& chmod +x /etc/init.d/logstash  
  
###############################################################################  
# CONFIGURATION  
###############################################################################  
  
### configure Logstash  
  
COPY ./config/logstash/logstash.yml $LOGSTASH_HOME/config/logstash.yml  
COPY ./config/logstash/logstash-jvm.options $LOGSTASH_HOME/config/jvm.options  
RUN chmod -R +r $LOGSTASH_HOME/config  
  
# filters & jaas  
COPY ./config/logstash/kafka-client-jaas.conf /etc/logstash/kafka-client-
jaas.conf  
COPY ./config/pipeline/00-kafka-input.conf /etc/logstash/conf.d/00-kafka-
input.conf  
COPY ./config/pipeline/11-filter.conf /etc/logstash/conf.d/11-filter.conf  
COPY ./config/pipeline/12-filter.conf /etc/logstash/conf.d/12-filter.conf  
COPY ./config/pipeline/30-output.conf /etc/logstash/conf.d/30-output.conf  
  
# Fix permissions  
RUN chmod -R +r /etc/logstash  
  
### configure logrotate  
  
COPY ./config/logstash/logstash-logrotate /etc/logrotate.d/logstash  
RUN chmod 644 /etc/logrotate.d/logstash  
  
###############################################################################  
# START  
###############################################################################  
  
COPY ./replace_ips.sh /usr/local/bin/replace_ips.sh  
COPY ./start.sh /usr/local/bin/start.sh  
  
RUN chmod +x /usr/local/bin/replace_ips.sh \  
&& chmod +x /usr/local/bin/start.sh  
  
VOLUME ["/etc/logstash/conf.d", "/var/lib/logstash"]  
EXPOSE 9600 5044  
  
CMD [ "/usr/local/bin/start.sh" ]  

