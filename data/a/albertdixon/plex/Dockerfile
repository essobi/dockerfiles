FROM debian:8  
MAINTAINER Albert Dixon <albert@dixon.rocks>  
  
ENTRYPOINT ["/bin/tini", "-g", "--", "/bin/entry"]  
CMD ["/bin/docker-start"]  
VOLUME ["/plexmediaserver"]  
EXPOSE 32400 33400 1900 5353 32410 32412 32413 32414 32469  
COPY dummy /bin/start  
COPY dummy /bin/systemctl  
COPY dummy /bin/service  
  
ENV FD_LIMIT=32768 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR=/plexmediaserver \  
PLEX_MEDIA_SERVER_HOME=/usr/lib/plexmediaserver \  
PLEX_MEDIA_SERVER_MAX_PLUGIN_PROCS=6 \  
PLEX_MEDIA_SERVER_MAX_STACK_SIZE=4000 \  
PLEX_MEDIA_SERVER_TMPDIR=/tmp \  
PLEX_MEDIA_SERVER_USER=plex \  
PLEX_UID=7000 \  
PLEX_GID=7000 \  
USE_TRAKT=yes \  
USE_UAS=yes \  
USE_SUBLIMINAL=no  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes --no-install-
recommends wget \  
&& wget -q --show-progress --progress=bar:force:noscroll -O -
http://shell.ninthgate.se/packages/shell.ninthgate.se.gpg.key | apt-key add -
\  
&& apt-get install -y --force-yes --no-install-recommends \  
avahi-daemon \  
avahi-utils \  
ca-certificates \  
curl \  
libssl-dev \  
locales \  
openssl \  
rsync \  
unzip \  
&& sed -i 's|# en_US.UTF-8|en_US.UTF-8|' /etc/locale.gen \  
&& locale-gen \  
&& DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales \  
&& useradd --create-home --user-group \  
\--home-dir ${PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR} \  
\--shell /bin/bash \  
\--uid ${PLEX_UID} plex \  
&& groupmod --gid ${PLEX_GID} plex  
  
ENV GOSU_VER=1.10 \  
PLEX_VER=1.3.3.3148-b38628e-debian \  
TINI_VER=v0.13.0  
RUN echo "deb http://shell.ninthgate.se/packages/debian plexpass main" >
/etc/apt/sources.list.d/plexmediaserver.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes --no-install-
recommends plexmediaserver=${PLEX_VER} \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /bin/gosu
"https://github.com/tianon/gosu/releases/download/${GOSU_VER}/gosu-$dpkgArch"
\  
&& wget -O /bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/${GOSU_VER}/gosu-$dpkgArch.asc"
\  
&& wget -O /bin/tini
"https://github.com/krallin/tini/releases/download/${TINI_VER}/tini" \  
&& wget -O /bin/tini.asc
"https://github.com/krallin/tini/releases/download/${TINI_VER}/tini.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \  
&& gpg --batch --verify /bin/gosu.asc /bin/gosu \  
&& gpg --batch --verify /bin/tini.asc /bin/tini \  
&& chmod +x /bin/tini /bin/gosu \  
&& wget -O /sublim.zip
https://github.com/bramwalet/Subliminal.bundle/archive/master.zip \  
&& wget -O /trakt.zip https://github.com/trakt/Plex-Trakt-
Scrobbler/archive/master.zip \  
&& wget -O /webtools.zip
https://github.com/dagalufh/WebTools.bundle/archive/master.zip \  
&& mkdir -p "${PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR}/Plex Media
Server/Plug-ins" \  
&& unzip /sublim.zip -d "${PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR}/Plex
Media Server/Plug-ins" \  
&& mv -v "${PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR}/Plex Media Server/Plug-
ins/Subliminal.bundle-master" \  
"${PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR}/Plex Media Server/Plug-
ins/Subliminal.bundle" \  
&& unzip /trakt.zip \  
&& mv -v "/Plex-Trakt-Scrobbler-master/Trakttv.bundle" \  
"${PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR}/Plex Media Server/Plug-ins/" \  
&& unzip /webtools.zip -d "${PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR}/Plex
Media Server/Plug-ins" \  
&& mv -v "${PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR}/Plex Media Server/Plug-
ins/WebTools.bundle-master" \  
"${PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR}/Plex Media Server/Plug-
ins/WebTools.bundle" \  
&& chown -R plex:plex "${PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR}" \  
&& apt-get autoremove -y && apt-get autoclean -y \  
&& /bin/gosu nobody true \  
&& rm -rvf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
/Plex-Trakt-Scrobbler-master /bin/*.asc \  
"$GNUPGHOME"  
  
COPY ["entry", "docker-start", "docker-test", "/bin/"]  
COPY preroll /preroll  
  
WORKDIR /usr/lib/plexmediaserver  
  
ARG BUILD_DATE=""  
ARG VCS_REF=""  
ARG VERSION="${PLEX_VER}"  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="plex" \  
org.label-schema.description="Plex Media Server" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/albertrdixon/docker-plex" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  

