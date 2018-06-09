FROM linuxserver/sonarr:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port="8989" \  
org.freenas.web-ui-path="" \  
org.freenas.port-mappings="8989:8989/tcp,9898:9898/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Database and Sonarr configs\" \  
}, \  
{ \  
\"name\": \"/tv\", \  
\"descr\": \"Location of TV library\" \  
}, \  
{ \  
\"name\": \"/scripts\", \  
\"descr\": \"Location of sickbeard-mp4-automator\" \  
}, \  
{ \  
\"name\": \"/downloads\", \  
\"descr\": \"Location of newsreader client downloads\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"PUID\", \  
\"descr\": \"SONARR USER ID\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PGID\", \  
\"descr\": \"SONARR GROUP ID\", \  
\"optional\": true \  
} \  
]" \  
org.freenas.static-volumes="[ \  
{ \  
\"container_path\": \"/dev/rtc\", \  
\"host_path\": \"/dev/rtc\", \  
\"readonly\": \"true\" \  
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
  

