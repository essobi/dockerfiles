FROM alpine:latest  
MAINTAINER kebyn <kebyn@sina.com>  
  
ENV LANG C.UTF-8  
ENV TZ Asia/Shanghai  
  
RUN set -ex \  
&& apk \--no-cache add \  
python3 \  
libmagic \  
ffmpeg \  
py3-numpy \  
py3-pillow \  
&& apk add --update --no-cache --virtual .deps \  
curl \  
tar \  
&& mkdir -p /opt/ehForwarderBot/storage \  
&& chmod +rw /opt/ehForwarderBot/storage  
  
WORKDIR /opt/ehForwarderBot  
  
RUN set -ex \  
&& curl -L -q -o ehForwarderBot.tar.gz \  
$( \  
curl -s https://api.github.com/repos/blueset/ehForwarderBot/tags | \  
grep tarball_url | head -n 1 | awk -F'"' '{print $4}'\  
) \  
&& tar xvf ehForwarderBot.tar.gz --strip-components=1 \  
&& rm -f ehForwarderBot.tar.gz \  
&& pip3 install -r requirements.txt \  
&& rm -rf /root/.cache \  
&& apk del .deps  
  
VOLUME /opt/ehForwarderBot/plugins/eh_telegram_master/tgdata.db  
  
ENTRYPOINT ["python3", "main.py"]  

