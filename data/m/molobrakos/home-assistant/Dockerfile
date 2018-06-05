FROM python:3.6-alpine3.7  
  
VOLUME /config  
WORKDIR /app  
  
RUN apk add --no-cache --update \  
dumb-init \  
gcc \  
g++ \  
make \  
musl-dev \  
linux-headers \  
nmap \  
libsodium \  
make \  
curl \  
libffi-dev \  
openssl-dev \  
ffmpeg \  
&& \  
pip3 install --no-cache-dir --upgrade colorlog cchardet cython uvloop
pywebpush \  
&& \  
rm -rf /root/.cache && \  
rm -rf /var/cache/apk/* \  
&& \  
adduser -H -D -s /bin/false home-assistant \  
&& \  
# https://github.com/gliderlabs/docker-alpine/issues/253  
chmod u+s /bin/ping \  
;  
  
EXPOSE 8123  
  
ENTRYPOINT ["dumb-init", "--"]  
  
HEALTHCHECK CMD curl --max-time 5 \--fail --silent --output /dev/null
http://localhost:8123/manifest.json || exit 1  

