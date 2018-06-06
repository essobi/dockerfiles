FROM python:2.7  
MAINTAINER carpenike <carpenike@gmail.com>  
  
# set version for s6 overlay  
ARG OVERLAY_VERSION="v1.18.1.5"  
ARG OVERLAY_ARCH="amd64"  
ADD https://github.com/just-
containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz
/tmp  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
# create ABC user  
RUN useradd -u 911 -U -d /config -s /bin/false abc && \  
usermod -G users abc && \  
  
# make our folders  
mkdir -p /app /config /defaults  
  
  
# Update PIP to support --no-cache-dir  
RUN pip install --no-cache-dir --upgrade \  
virtualenv \  
cheetah \  
configparser \  
  
ndg-httpsclient \  
notify \  
paramiko \  
pillow \  
pip-review\  
psutil \  
pyopenssl \  
requests \  
urllib3  
  
RUN pip-review --local \--auto  
  
# add local files  
COPY root/ /  
  
ENTRYPOINT ["/init"]  

