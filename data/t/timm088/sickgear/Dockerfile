FROM python:2.7-alpine  
  
RUN apk -U upgrade && \  
apk add --no-cache \  
ca-certificates \  
wget \  
git \  
openssl \  
tar \  
curl \  
tzdata \  
libxml2 \  
libxml2-dev \  
libxslt \  
libxslt-dev \  
musl-dev \  
gcc && \  
\  
pip install --no-cache-dir \  
lxml && \  
\  
adduser -u 1001 -S media -G users && \  
mkdir /data /tvseries && \  
chown -R media:users /data /tvseries && \  
\  
git clone --depth=1 https://github.com/SickGear/SickGear /sickgear && \  
chown -R media:users /sickgear && \  
\  
pip install --no-cache-dir -r /sickgear/requirements.txt && \  
\  
apk del \  
gcc \  
libxml2-dev \  
libxslt-dev \  
wget \  
musl-dev  
  
EXPOSE 8081  
  
USER media  
  
VOLUME ["/data", "/tvseries"]  
  
CMD ["/usr/local/bin/python", "/sickgear/SickBeard.py", "--datadir", "/data",
"--config", "/data/config.ini"]  

