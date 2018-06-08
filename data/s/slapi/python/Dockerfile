  
FROM slapi/base:latest  
  
MAINTAINER SLAPI Devs  
  
# A lot of work borrowed from https://github.com/jfloff/alpine-python  
# Add testing and community repositories -- community is untagged as tagging
it causes odd issues with the package index  
RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories &&\  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories &&\  
# Add the packages, with a CDN-breakage fallback if needed  
apk add --no-cache \  
musl \  
build-base \  
ca-certificates \  
python \  
python-dev \  
py-pip \  
py-setuptools || \  
(sed -i -e 's/dl-cdn/dl-4/g' /etc/apk/repositories apk add --no-cache
$PACKAGES) &&\  
# make some useful symlinks that are expected to exist  
if [[ ! -e /usr/bin/python ]]; then ln -sf
/usr/bin/python${PYTHON_MAJOR_VERSION} /usr/bin/python; fi &&\  
if [[ ! -e /usr/bin/python-config ]]; then ln -sf
/usr/bin/python${PYTHON_MAJOR_VERSION}*-config /usr/bin/python-config; fi &&\  
  
pip install --upgrade pip &&\  
# Install libraries and tools  
pip install \  
awscli \  
requests \  
arrow \  
httpie &&\  
# Cleanup  
rm -rf /tmp/* /var/cache/apk/* /root/.cache/pip  

