FROM ubuntu:bionic-20180125  
  
ARG APT_PROXY  
ARG APT_PROXY_SSL  
ENV DEBIAN_FRONTEND="noninteractive" \  
SYSTEM_USER="ubuntu" \  
SYSTEM_USER_UID="1000" \  
SYSTEM_USER_GID="1000" \  
TZ="Europe/London" \  
LANG="en_GB.UTF-8" \  
LC_ALL="en_GB.UTF-8" \  
INIT_DEBUG="false" \  
INIT_TRACE="false" \  
INIT_GOSU="true" \  
INIT_RUN_AS=""  
  
RUN set -ex; \  
\  
# set internal variables  
GOSU_VERSION="1.10"; \  
GOSU_DOWNLOAD_URL="https://github.com/tianon/gosu/releases/download"; \  
GOSU_GPG_KEY="B42F6819007F00F88E364FD4036A9C25BF357DD4"; \  
\  
# install system packages  
if [ -n "$APT_PROXY" ]; then echo "Acquire::http { Proxy
\"http://${APT_PROXY}\"; };" > /etc/apt/apt.conf.d/00proxy; fi; \  
if [ -n "$APT_PROXY_SSL" ]; then echo "Acquire::https { Proxy
\"https://${APT_PROXY_SSL}\"; };" > /etc/apt/apt.conf.d/00proxy; fi; \  
echo "APT::Install-Recommends 0;\nAPT::Install-Suggests 0;" >>
/etc/apt/apt.conf.d/01norecommends; \  
apt-get --yes update; \  
apt-get --yes upgrade; \  
apt-get --yes install \  
ca-certificates \  
curl \  
dirmngr \  
gnupg \  
locales \  
; \  
# SEE: https://github.com/tianon/gosu  
curl -L "$GOSU_DOWNLOAD_URL/$GOSU_VERSION/gosu-amd64" -o /usr/local/bin/gosu;
\  
curl -L "$GOSU_DOWNLOAD_URL/$GOSU_VERSION/gosu-amd64.asc" -o
/usr/local/bin/gosu.asc; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys $GOSU_GPG_KEY;
\  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -rf $GNUPGHOME /usr/local/bin/gosu.asc; \  
chmod +x /usr/local/bin/gosu; \  
gosu nobody true; \  
\  
# SEE: https://github.com/stefaniuk/dotfiles  
curl -L https://raw.githubusercontent.com/stefaniuk/dotfiles/master/dotfiles
-o - | /bin/bash -s -- \  
\--minimal \  
; \  
# configure system user  
groupadd --system --gid $SYSTEM_USER_GID $SYSTEM_USER; \  
useradd --system --create-home --uid $SYSTEM_USER_UID --gid $SYSTEM_USER_GID
$SYSTEM_USER; \  
locale-gen $LANG; \  
\  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/apt/*; \  
rm -f /etc/apt/apt.conf.d/00proxy  
  
COPY assets/ /  
  
ENTRYPOINT [ "/sbin/entrypoint.sh" ]  
  
### METADATA
###################################################################  
  
ARG IMAGE  
ARG BUILD_DATE  
ARG VERSION  
ARG VCS_REF  
ARG VCS_URL  
LABEL \  
org.label-schema.name=$IMAGE \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.schema-version="1.0"  

