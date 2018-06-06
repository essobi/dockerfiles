FROM docker:latest  
  
RUN set -x \  
&& apk add --no-cache \  
python2 \  
bash \  
curl \  
&& apk add --no-cache --virtual build-deps \  
make \  
py-pip \  
wget \  
&& pip install --trusted-host pypi.python.org \  
docker-compose \  
&& wget
https://github.com/geofffranks/spruce/releases/download/v1.12.1/spruce-linux-
amd64 \  
&& chmod +x spruce-linux-amd64 && mv spruce-linux-amd64 /usr/local/bin/spruce
\  
&& rm -r ~/.cache/pip \  
&& apk del build-deps  

