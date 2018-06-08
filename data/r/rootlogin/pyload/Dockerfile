FROM rootlogin/python2:latest  
MAINTAINER Simon Erhardt <me+docker@rootlogin.ch>  
  
ARG UID=1502  
ARG GID=1502  
RUN apk add --update \  
wget \  
curl \  
unrar \  
py-curl \  
py-simplejson \  
py-feedparser \  
py-crypto \  
unzip \  
perl \  
ca-certificates \  
gcc \  
python-dev \  
musl-dev \  
libffi-dev \  
openssl-dev \  
jpeg-dev \  
git  
  
RUN addgroup -g ${GID} pyload \  
&& adduser -u ${UID} -h /opt/pyload -H -G pyload -s /bin/sh -D pyload  
  
RUN mkdir /opt \  
&& cd /opt \  
&& git clone https://github.com/pyload/pyload.git --depth 1 -b stable -o
pyload \  
&& rm -rf pyload/.git  
  
RUN pip install \  
baker \  
pyOpenSSL \  
Spidermonkey  
  
RUN apk del \  
wget \  
perl \  
gcc \  
python-dev \  
musl-dev \  
libffi-dev \  
openssl-dev \  
jpeg-dev \  
git \  
&& rm -rf /var/cache/apk/*  
  
COPY config/* /tmp/pyload-config/  
COPY run.sh /opt/pyload/run.sh  
RUN chmod +x /opt/pyload/run.sh  
  
VOLUME ["/config"]  
  
EXPOSE 8000  
CMD ["/opt/pyload/run.sh"]  

