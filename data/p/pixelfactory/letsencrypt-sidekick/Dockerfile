FROM alpine:latest  
MAINTAINER Amine Benseddik <amine.benseddik@gmail.com>  
  
ENV LEGO_VERSION="v0.3.1"  
  
ENV PYTHON_MAJOR_VERSION=2  
# Install needed packages. Notes:  
# * dumb-init: a proper init system for containers, to reap zombie children  
# * bash: so we can access /bin/bash  
ENV PACKAGES="\  
dumb-init \  
musl \  
build-base \  
bash \  
openssl \  
ca-certificates \  
python${PYTHON_MAJOR_VERSION} \  
py-setuptools \  
"  
  
RUN echo \  
# Figure out the minor version from the binary name  
# no real need for this variable at the moment  
# && PYTHON_MINOR_VERSION="$(find /usr/bin -type f -name python\\* | sort |
tail -n1 | cut -d'.' -f2 | cut -d'-' -f1)" \  
# Unfortunately the Alpine repositories are in a slightly inconsistent state
for now-- python2 only exists in 'edge', not main.  
&& if [[ "$PYTHON_MAJOR_VERSION" == '2' ]]; then PACKAGES="$(echo $PACKAGES |
sed -e 's/python2/python/g')"; fi \  
  
# Add testing and community repositories -- community is untagged as tagging
it causes odd issues with the package index  
&& echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
  
# Add the packages, with a CDN-breakage fallback if needed  
&& apk add --no-cache $PACKAGES || \  
(sed -i -e 's/dl-cdn/dl-4/g' /etc/apk/repositories && apk add --no-cache
$PACKAGES) \  
  
# make some useful symlinks that are expected to exist  
&& if [[ ! -e /usr/bin/python ]]; then ln -sf
/usr/bin/python${PYTHON_MAJOR_VERSION} /usr/bin/python; fi \  
&& if [[ ! -e /usr/bin/python-config ]]; then ln -sf
/usr/bin/python${PYTHON_MAJOR_VERSION}*-config /usr/bin/python-config; fi \  
  
&& if [[ ! -e /usr/bin/easy_install ]]; then ln -sf
/usr/bin/easy_install-${PYTHON_MAJOR_VERSION}.* /usr/bin/easy_install; fi \  
  
# Install and upgrade Pip  
&& easy_install pip \  
&& pip install --upgrade pip \  
  
# Add Lego (LetsEncrypt Go) https://github.com/xenolf/lego  
&& mkdir /opt \  
&& wget -O /opt/lego_linux_amd64-$LEGO_VERSION.tar.xz
https://github.com/xenolf/lego/releases/download/$LEGO_VERSION/lego_linux_amd64.tar.xz
\  
&& tar -xvf /opt/lego_linux_amd64-$LEGO_VERSION.tar.xz -C /opt \  
&& rm -f /opt/lego_linux_amd64-$LEGO_VERSION.tar.xz \  
&& echo  
  
ADD pixel /opt/pixel  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["/opt/pixel/start.py"]  

