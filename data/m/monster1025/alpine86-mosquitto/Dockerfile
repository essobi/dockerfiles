FROM gliderlabs/alpine  
MAINTAINER monster1025, https://github.com/monster1025  
  
# Install needed packages. Notes:  
# * dumb-init: a proper init system for containers, to reap zombie children  
# * musl: standard C library  
# * linux-headers: commonly needed, and an unusual package name from Alpine.  
# * build-base: used so we include the basic development packages (gcc)  
# * bash: so we can access /bin/bash  
# * git: to ease up clones of repos  
# * ca-certificates: for SSL verification during Pip and easy_install  
# * python: the binaries themselves  
# * python-dev: are used for gevent e.g.  
# git \  
ENV PACKAGES="\  
dumb-init \  
bash \  
mosquitto \  
mosquitto-clients \  
"  
ADD run.sh /run.sh  
  
RUN echo \  
# replacing default repositories with edge ones  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
  
# Add the packages, with a CDN-breakage fallback if needed  
&& apk add \--no-cache $PACKAGES || \  
(sed -i -e 's/dl-cdn/dl-4/g' /etc/apk/repositories && apk add --no-cache
$PACKAGES) \  
  
# turn back the clock -- so hacky!  
&& echo "http://dl-cdn.alpinelinux.org/alpine/v3.4/main/" >
/etc/apk/repositories \  
# && echo "@edge-testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
# && echo "@edge-community http://dl-
cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \  
# && echo "@edge-main http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
  
&& rm -rf /var/cache/apk/* \  
&& chmod +x run.sh  
  
#USER nobody  
EXPOSE 1883  
ENTRYPOINT ["/usr/bin/dumb-init"]  
CMD ["/run.sh"]

