FROM python:3.5-slim  
MAINTAINER Shiqiao Du <lucidfrontier.45@gmail.com>  
  
RUN set -ex \  
&& buildDeps=' \  
gcc \  
libbz2-dev \  
libc6-dev \  
libpcre3-dev \  
libssl-dev \  
make \  
pax-utils \  
zlib1g-dev \  
' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install --no-cache-dir uwsgi \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u | cut -c4- \  
| xargs dpkg --search \  
| cut -d ':' -f 1 | sort -u \  
)" \  
&& apt-get install -y --no-install-recommends $runDeps \  
&& apt-get purge -y --auto-remove $buildDeps  
  
COPY mime.types /etc/mime.types  

