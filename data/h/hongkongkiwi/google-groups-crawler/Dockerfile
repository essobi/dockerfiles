FROM node:9.11.1-alpine  
  
MAINTAINER Andy Savage <andy@savage.hk>  
  
LABEL org.label-schema.name="google-group-crawler" \  
org.label-schema.description="Docker Image to handle downloading attachment
files from Google Groups and sending to an AMQP queue" \  
org.label-schema.vcs-url="https://github.com/hongkongkiwi/google-group-
crawler" \  
org.label-schema.license="MIT"  
  
ARG OS="linux"  
ARG ARCH="amd64"  
# URLS for stuff to install during build  
ARG SUPERCRONIC_VER="0.1.5"  
ARG
SUPERCRONIC_URL="https://github.com/aptible/supercronic/releases/download/v${SUPERCRONIC_VER}/supercronic-${OS}-${ARCH}"  
ARG SUPERCRONIC_SHA1SUM='9aeb41e00cc7b71d30d33c57a2333f2c2581a201'  
ARG S6_OVERLAY_VERSION="1.21.4.0"  
ARG S6_OVERLAY_URL="https://github.com/just-
containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-${ARCH}.tar.gz"  
ARG GOOGLE_CRAWLER_VERSION="1.2.1"  
ARG GOOGLE_CRAWLER_URL="https://github.com/icy/google-group-
crawler/archive/v${GOOGLE_CRAWLER_VERSION}.tar.gz"  
# ARG
QUICK_LOCK_REPO='https://raw.githubusercontent.com/oresoftware/quicklock/master/install.sh'  
ARG RCLONE_VER="current"  
ARG
RCLONE_URL="https://downloads.rclone.org/rclone-${RCLONE_VER}-${OS}-${ARCH}.zip"  
# ARG
BLOG_URL='https://raw.githubusercontent.com/idelsink/b-log/master/b-log.sh'  
# Some options that can be configured  
ENV CRON_SCHEDULE='*/30 * * * *'  
# Which files do we want to trigger our hook on  
ENV WATCH_FILE_PATTERN='*.xls'  
# Where we can find the cookies file for authing to google groups  
ENV COOKIES_FILE='/config/cookies.txt'  
# You shouldn't need to change this unless you want to change the hook script  
ENV HOOK_FILE='/google-group-crawler/hook.sh'  
ENV GOOGLE_GROUP_NAME=''  
# This is important when dealing with Google Group in organisation  
ENV GOOGLE_GROUP_ORG=''  
# How many messages to get when updating via RSS  
ENV UPDATE_MESSAGE_COUNT=50  
# Set this to force pull down all messages  
ENV FORCE_REFRESH='false'  
# If you only want messages you can change this  
ENV DOWNLOAD_ATTACHMENTS='true'  
# This will produce a lot of noise and is not recommended unless you need a
full pull  
ENV PULL_ON_BOOT='true'  
# Mostly useful for the cron script  
ENV TZ='Asia/Hong_Kong'  
# Ignore the noisy NPM installs  
ENV NPM_CONFIG_LOGLEVEL='error'  
# Upload files we find to rclone remote (e.g. Google Groups)  
ENV RCLONE_UPLOAD='false'  
# Which rclone remote to upload to  
ENV RCLONE_REMOTE='Google Drive'  
# Send files found to AQMP server?  
ENV AMQP_ENABLED='false'  
# AMQP Server info  
ENV AMQP_URL=''  
ENV AMQP_EXCHANGE='google_groups'  
ENV AMQP_QUEUE='google_groups_changes'  
# Send files found to Kafka Rest server?  
ENV KAFKA_ENABLED='false'  
# Kafka Rest Server info  
ENV KAFKA_REST_URL='http://kafka-rest:8082'  
ENV KAFKA_REST_TOPIC='production-reports'  
ENV PGID=1001 \  
PUID=1001  
ENV PS1="$(whoami)@$(hostname):$(pwd)\$ " \  
HOME="/root" \  
TERM="xterm" \  
PATH="${PATH}:/usr/local/bin:/usr/local/sbin"  
# Path to Python (required for some NPM builds)  
ENV PYTHON="/usr/bin/python"  
# Path to b-log.sh which is downloaded for bash logging  
ENV BLOG="/usr/local/include/b-log.sh"  
ENV SUPERCRONIC="/usr/local/bin/supercronic"  
VOLUME ["/data", "/config"]  
  
# Copy all our awesome scripts to the bin  
COPY scripts/* /usr/local/bin/  
COPY ldb/manpages/ldb.1 /usr/share/man/man1  
COPY ldb/bin/ldb /usr/local/bin/ldb  
COPY blog/b-log.sh "${BLOG}"  
COPY quicklock/install.sh /tmp/qlinstall.sh  
COPY s6/ /etc  
  
# install dependencies  
RUN echo "@edgecommunity http://dl-cdn.alpinelinux.org/alpine/edge/community"
>> /etc/apk/repositories \  
#&& echo "@edgetesting http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
#&& echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
# Add community repo \  
&& apk update \  
#&& apk add --upgrade apk-tools@edge \  
# make g++ snappy-dev gcc cmake@edge \  
# unzip \  
# git \ \  
# && apk add cmake@edge \  
# netcat-openbsd \  
# Install these as a group so they are easy to remove \  
&& apk add --no-cache --virtual .build-dependencies \  
tzdata \  
py2-pip \  
&& apk add --no-cache \  
shadow \  
curl \  
snappy \  
ca-certificates \  
bash gawk sed grep wget coreutils procps \  
rabbitmq-c-utils \  
python3 \  
python3-dev \  
python \  
yaml-dev \  
musl-dev \  
ripmime@edgecommunity \  
&& mkdir -p \  
"/usr/local/include" \  
"/usr/local/bin" \  
"/usr/local/sbin" \  
"/tmp" \  
"/var/log/supercronic" \  
"/var/log/watchdog"  
  
RUN mkdir -p "/usr/share/man/man1" >/dev/null 2>&1 || true  
  
# Set the time  
RUN echo "Setting Time Zone" \  
&& cp "/usr/share/zoneinfo/${TZ}" /etc/localtime \  
&& echo "${TZ}" > /etc/timezone  
  
RUN echo "Adding User/Group" \  
&& addgroup -g ${PGID} abc \  
&& adduser -D -u ${PUID} -G abc abc \  
&& usermod -G users abc  
# && adduser -D -u 32768 -G abc nobody  
# Installing Logging Libraries  
ADD "$SUPERCRONIC_URL" "$SUPERCRONIC"  
ADD "$S6_OVERLAY_URL" "/tmp/s6-overlay-${ARCH}.tar.gz"  
RUN bash "/tmp/qlinstall.sh" \  
&& echo "Verifying Supercronic" \  
&& echo "${SUPERCRONIC_SHA1SUM} /usr/local/bin/supercronic" | sha1sum -c - \  
&& echo "Extracting S6 Overlay" \  
&& tar xzf "/tmp/s6-overlay-${ARCH}.tar.gz" -C /  
  
# Download Google Group Crawler bash scripts  
ADD "${GOOGLE_CRAWLER_URL}" "/tmp/google-group-crawler.tar.gz"  
RUN echo "Installing Google Group Crawler" \  
&& ([ -d /google-group-crawler ] && rm -Rf /google-group-crawler || true) \  
&& mkdir -p /google-group-crawler \  
&& tar xzf "/tmp/google-group-crawler.tar.gz" -C /google-group-crawler  
COPY hook.sh "$HOOK_FILE"  
  
# Upgrade PIP  
RUN echo "Upgrading Pip & Installing Watchdog" \  
&& pip3 install -q --no-cache-dir --upgrade pip \  
&& pip3 install -q --no-cache-dir watchdog \  
&& pip2 install -q --no-cache-dir crudini  
  
# Install rclone  
RUN echo "Installing rclone" \  
&& cd /tmp \  
&& wget -q "${RCLONE_URL}" \  
&& unzip -qq /tmp/rclone-*.zip \  
&& mv /tmp/rclone-*-${OS}-*/rclone /usr/local/bin \  
&& mkdir -p /var/lock \  
&& touch /var/lock/rclone.lock  
  
# clean up dependencies  
RUN echo "Cleaning Up" \  
&& chmod -R +x /usr/local/bin /usr/sbin /usr/local/sbin \  
&& apk del --purge .build-dependencies \  
&& rm -rf \  
/tmp/* \  
/var/tmp/* \  
/var/cache/apk/* \  
~/.cache/pip  
  
WORKDIR /data  
  
ENTRYPOINT ["/init"]  

