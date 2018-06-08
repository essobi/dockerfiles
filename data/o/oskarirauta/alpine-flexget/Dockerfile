FROM oskarirauta/alpine:latest  
MAINTAINER Oskari Rauta <oskari.rauta@gmail.com>  
  
VOLUME /config  
VOLUME /data/downloads  
VOLUME /data/incomplete  
VOLUME /media/series  
VOLUME /media/movies  
  
EXPOSE 3539  
ENV PUID=""  
ENV PGID=""  
ENV WEBUI_PASSWORD=""  
ENV TRAKT_USERID=""  
RUN apk add --update --no-cache python py2-pip ca-certificates wget nano
tzdata bash shadow curl sqlite sudo dcron findutils openssl \  
&& apk add --update --no-cache --repository "http://dl-
cdn.alpinelinux.org/alpine/edge/testing" \--repository "http://dl-
cdn.alpinelinux.org/alpine/edge/main" \  
libressl2.5-libcrypto libtorrent-rasterbar \  
&& apk add --update --no-cache --virtual .build-deps \  
build-base bzip2-dev python2-dev openssl-dev libffi-dev openssl-dev \  
&& update-ca-certificates \  
&& pip install --no-cache-dir --upgrade pip \  
&& pip install --no-cache-dir --upgrade --force-reinstall setuptools
requests[security]  
  
RUN pip install --no-cache-dir --upgrade --force-reinstall six  
RUN pip install --no-cache-dir --upgrade --force-reinstall BeautifulSoup  
RUN pip install --no-cache-dir --upgrade transmissionrpc  
RUN pip install --no-cache-dir --upgrade cfscrape  
RUN pip install --no-cache-dir --upgrade "subliminal>=2.0.5"  
RUN pip install --no-cache-dir --upgrade flexget  
  
RUN addgroup -S -g 2001 media \  
&& adduser -SH -u 1001 -G media -s /sbin/nologin -h /config flexget \  
&& rm -rf /var/cache/apk/** \  
&& mkdir -p /etc/flexget/plugins  
  
COPY config/config.yml /etc/flexget/config.yml  
COPY config/secrets.yml /etc/flexget/secrets.yml  
COPY config/series.yml /etc/flexget/series.yml  
  
COPY config/plugins/log_filter.py /etc/flexget/plugins/log_filter.py  
COPY config/plugins/forget_series.py /etc/flexget/plugins/forget_series.py  
  
COPY init/flexget /etc/init.d/flexget  
COPY /cron/root /etc/crontabs/root  
  
RUN apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
  
RUN rc-update add flexget default \  
&& rc-update add dcron default  

