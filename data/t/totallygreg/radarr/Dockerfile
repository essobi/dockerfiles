FROM linuxserver/radarr:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="2" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port="7878" \  
org.freenas.web-ui-path="" \  
org.freenas.port-mappings="7878:7878/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Config storage space\" \  
}, \  
{ \  
\"name\": \"/downloads\", \  
\"descr\": \"Downloads volume\" \  
}, \  
{ \  
\"name\": \"/scripts\", \  
\"descr\": \"Location of sickbeard-mp4-automator\" \  
}, \  
{ \  
\"name\": \"/movies\", \  
\"descr\": \"Movies volume\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"TZ\", \  
\"descr\": \"Timezone - eg Europe/London\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PGID\", \  
\"descr\": \"GroupID\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PUID\", \  
\"descr\": \"UserID\", \  
\"optional\": true \  
} \  
]"  
  
# OS update & package installation  
RUN \  
apt-get update && \  
apt-get install -y \  
ca-certificates \  
ffmpeg \  
git \  
python-pip \  
openssl \  
python-dev \  
libffi-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
tzdata \  
zlib1g-dev  
  
# pip package installation  
RUN pip install --upgrade pip && \  
pip --no-cache-dir install --upgrade setuptools && \  
pip --no-cache-dir install --upgrade pyopenssl \  
requests \  
requests[security] \  
requests-cache \  
cheetah \  
babelfish \  
"guessit<2" \  
"subliminal<2" \  
stevedore==1.19.1 \  
python-dateutil \  
deluge-client \  
qtfaststart \  
requirements  
  
RUN cp /usr/share/zoneinfo/US/Eastern /etc/localtime  
  
WORKDIR /tmp  
  
# clone ffmpeg  
#RUN wget -q https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-
static.tar.xz && \  
# tar xJf ffmpeg-release-64bit-static.tar.xz && \  
# mv ffmpeg-*-64bit-static/ffmpeg /usr/local/bin/ && \  
# mv ffmpeg-*-64bit-static/ffprobe /usr/local/bin/ && \  
# rm -rf ffmpeg*  
  
  
# Cleanup  

