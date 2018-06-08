FROM ubuntu:16.04  
  
MAINTAINER Sebastien Allamand "sebastien@allamand.com"  
  
  
ENV LANG=C.UTF-8 \  
DEBIAN_FRONTEND=noninteractive \  
DEBCONF_NONINTERACTIVE_SEEN=true \  
SYNCTHING_VERSION=0.14.41 \  
GOSU_VERSION=1.10  
  
###TODO: ajouter un check sur version SYNCTHONG et GOSU  
# check latest version at
https://github.com/syncthing/syncthing/releases/latest  
# Check latest version at https://github.com/tianon/gosu/releases/latest  
  
  
RUN set -x \  
&& apt-get update \  
&& apt-get upgrade -y --no-install-recommends \  
&& apt-get install curl wget ca-certificates -y --no-install-recommends \  
  
  
#Install GOSU source https://github.com/tianon/gosu  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg \--keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg \--batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
  
  
&& apt-get purge -y --auto-remove -y wget \  
&& apt-get clean  
  
  
  
  
  
ARG VCF_REF  
ARG BUILD_DATE  
LABEL org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="MIT" \  
org.label-schema.name="syncthing" \  
org.label-schema.url="https://syncthing.net/" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/allamand/docker-syncthing" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF  
  
  
ARG MYUSERNAME=syncthing  
ARG MYGROIUPNAME=sync  
ARG MYUID=1000  
ARG MYGID=1000  
ENV USERNAME=${MYUSERNAME} \  
GROUPNAME=${MYGROUPNAME} \  
UID=${MYUID} \  
GID=${MYGID}  
  
# get syncthing  
WORKDIR /srv  
  
RUN echo 'Creating user: ${MYUSERNAME} with UID $UID' \  
&& groupadd -g $GID sync \  
&& useradd --uid $UID --no-create-home -g sync $USERNAME  
#RUN useradd --no-create-home -g users syncthing  
  
  
RUN curl -L -o syncthing.tar.gz
https://github.com/syncthing/syncthing/releases/download/v$SYNCTHING_VERSION/syncthing-
linux-amd64-v$SYNCTHING_VERSION.tar.gz \  
&& tar -xzvf syncthing.tar.gz \  
&& rm -f syncthing.tar.gz \  
&& mv syncthing-linux-amd64-v* syncthing \  
&& rm -rf syncthing/etc \  
&& rm -rf syncthing/*.pdf \  
&& mkdir -p /srv/config \  
&& mkdir -p /srv/data  
  
VOLUME ["/srv/data", "/srv/config"]  
  
ADD ./entrypoint.sh /srv/entrypoint.sh  
RUN chmod 770 /srv/entrypoint.sh && chown -R $USERNAME:$GROUPNAME /srv/  
  
#USER $USERNAME  
  
ENTRYPOINT ["/srv/entrypoint.sh"]  
  
#CMD ["bash"]  

