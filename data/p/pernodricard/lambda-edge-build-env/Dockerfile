FROM node:6-alpine  
  
ENV PACKAGES="\  
dumb-init \  
musl \  
linux-headers \  
build-base \  
bash \  
git \  
ca-certificates \  
python2 \  
python2-dev \  
py-setuptools \  
zip \  
groff \  
less \  
jq \  
openssh-client \  
"  
  
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
&& echo "http://dl-cdn.alpinelinux.org/alpine/v$ALPINE_VERSION/main/" >
/etc/apk/repositories \  
  
# make some useful symlinks that are expected to exist  
&& if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python2.7
/usr/bin/python; fi \  
&& if [[ ! -e /usr/bin/python-config ]]; then ln -sf /usr/bin/python2.7-config
/usr/bin/python-config; fi \  
&& if [[ ! -e /usr/bin/easy_install ]]; then ln -sf /usr/bin/easy_install-2.7
/usr/bin/easy_install; fi \  
  
# Install and upgrade Pip  
&& easy_install pip \  
&& pip install \--upgrade pip \  
&& if [[ ! -e /usr/bin/pip ]]; then ln -sf /usr/bin/pip2.7 /usr/bin/pip; fi  
  
WORKDIR /base  
COPY requirements.txt /base  
RUN pip install -r requirements.txt  
COPY scripts /base/scripts  
  
ENTRYPOINT ["/usr/bin/dumb-init"]  
CMD /bin/bash  

