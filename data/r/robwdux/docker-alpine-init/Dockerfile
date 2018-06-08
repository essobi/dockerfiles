FROM robwdux/alpine-base:3.4  
MAINTAINER rob dux <robwdux@gmail.com>  
  
ENTRYPOINT ["/init"]  
  
WORKDIR /etc/services.d  
  
ARG S6_VERSION  
  
ENV S6_VERSION=${S6_VERSION:-1.18.1.3} \  
# do not reset container env  
S6_KEEP_ENV=1 \  
# log to stdout and stderr for all services  
S6_LOGGING=0 \  
# warn but continue if any stage 2 code fails  
S6_BEHAVIOUR_IF_STAGE2_FAILS=1 \  
SVC_TDIR=/etc/s6/svc-templates \  
SVC_DIR=/etc/services.d  
  
RUN set -o nounset -o errexit -o xtrace -o verbose \  
&& apk add --no-cache --virtual .buildDeps \  
gnupg \  
&& mkdir /usr/src && cd /usr/src \  
&& curl -fsSLO \  
https://github.com/just-
containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz
\  
&& curl -fsSLO \  
https://github.com/just-
containers/s6-overlay/releases/download/v1.18.1.3/s6-overlay-amd64.tar.gz.sig
\  
&& gpg --keyserver pgp.mit.edu --recv-key 0x337EE704693C17EF \  
&& gpg --verify s6-overlay-amd64.tar.gz.sig s6-overlay-amd64.tar.gz \  
&& tar -C / -zxf s6-overlay-amd64.tar.gz \  
# stage services, template scripts. symlink service to $SVC_DIR to enable  
&& mkdir -p $SVC_TDIR \  
&& echo "#!/usr/bin/with-contenv sh" \  
> ${SVC_TDIR}/run.container.env \  
&& echo -e "#!/bin/sh\ns6-svscanctl -t /var/run/s6/services" \  
> ${SVC_TDIR}/finish.stop.containers \  
&& chmod -R +x ${SVC_TDIR}/* \  
# purge  
&& apk del --purge .buildDeps \  
&& cd && rm -vrf /usr/src /root/* /tmp/*  
  
  
#m### COMMIT - git show -s --format=%H  
# DATE - git show -s --format=%cI  
# AUTHOR - git show -s --format='"%an" <%ae>'  
# URL - git ls-remote --get-url | sed -e "s|:|/|" -e s|git@|https://|"  
ARG GIT_COMMIT=""  
ARG GIT_COMMIT_DATE=""  
ARG GIT_COMMIT_AUTHOR=""  
ARG GIT_REPO_URL=""  

