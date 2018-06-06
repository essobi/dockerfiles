FROM lsiobase/alpine  
MAINTAINER sparklyballs  
  
# package version  
# (stable-download or testing-download)  
ARG NZBGET_BRANCH="stable-download"  
# install packages  
RUN \  
apk add --no-cache \  
curl \  
p7zip \  
python \  
unrar \  
wget \  
git \  
unzip \  
tar \  
ffmpeg  
  
# install nzbget  
RUN \  
curl -o \  
/tmp/json -L \  
http://nzbget.net/info/nzbget-version-linux.json && \  
NZBGET_VERSION=$(grep "${NZBGET_BRANCH}" /tmp/json | cut -d '"' -f 4) && \  
curl -o \  
/tmp/nzbget.run -L \  
"${NZBGET_VERSION}" && \  
sh /tmp/nzbget.run --destdir /app && \  
  
# cleanup  
rm -rf \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
# install nzbToMedia  
RUN \  
mkdir /scripts  
  
RUN \  
git clone https://github.com/clinton-hall/nzbToMedia.git /scripts  
  
RUN \  
ln -sf /usr/bin/python2.7 /usr/bin/python2  
  
# ports and volumes  
VOLUME /config /downloads  
EXPOSE 6789  

