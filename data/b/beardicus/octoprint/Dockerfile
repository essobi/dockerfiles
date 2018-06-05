FROM python:2.7-slim  
MAINTAINER Brian Boucheron <brian@boucheron.org>  
  
RUN set -ex \  
&& runDeps=' \  
git \  
gcc \  
g++ \  
make \  
wget \  
ffmpeg \  
ca-certificates \  
linux-headers-3.16.0-4-amd64 \  
' \  
&& echo 'deb http://deb.debian.org/debian jessie-backports main' >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y $runDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone https://github.com/foosel/OctoPrint.git \  
&& cd /OctoPrint \  
&& python setup.py install \  
&& mkdir /data  
  
VOLUME /data  
EXPOSE 5000  
COPY config-defaults.yaml /  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["octoprint", "serve", "--iknowwhatimdoing", "--basedir", "/data"]  

