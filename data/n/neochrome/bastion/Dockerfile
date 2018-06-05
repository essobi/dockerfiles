# vim: ft=dockerfile  
FROM alpine:edge  
ARG GA_VERSION=1.02  
LABEL \  
description="Bastion with google authenticator" \  
maintainer="johan@stenqvist.net" \  
google.authenticator.version=$GA_VERSION  
  
RUN apk --update add \  
openssh-server-pam linux-pam \  
build-base automake autoconf libtool curl tar linux-pam-dev \  
&& mkdir -p /src/ga \  
&& curl -L https://github.com/google/google-
authenticator/tarball/${GA_VERSION} \  
| tar -xzvf - -C /src/ga --strip-components 1 \  
&& (cd /src/ga/libpam \  
&& ./bootstrap.sh \  
&& ./configure \  
\--prefix=/ \  
&& make \  
&& make install) \  
&& rm -rf /src \  
&& apk del \  
build-base automake autoconf libtool curl tar linux-pam-dev \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /etc/ssh/ssh_host_*_key* \  
&& rm -f /etc/motd  
  
COPY ./sshd_config /etc/ssh/  
COPY ./sshd.pam /etc/pam.d/sshd  
  
RUN adduser -D -G users -s /bin/sh -h /bastion bastion \  
&& passwd -u bastion  
RUN echo '[[ -e .google_authenticator ]] || google-authenticator' >>
/etc/profile  
  
EXPOSE 22  
VOLUME /etc/ssh /bastion  
CMD ssh-keygen -A && /usr/sbin/sshd -De  

