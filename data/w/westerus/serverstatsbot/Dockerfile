FROM python:3.4-slim  
LABEL Maintainer="westerus@gmail.com" \  
Name="ServerStatsBot" \  
Description="Image of Telegram Bot ServerStatsBot" \  
Version="1.0.0"  
  
ARG APT_FLAGS_COMMON="-qq -y"  
ARG APT_FLAGS_PERSISTANT="${APT_FLAGS_COMMON} --no-install-recommends"  
ARG APT_FLAGS_DEV="${APT_FLAGS_COMMON} --no-install-recommends"  
ARG APTUPDATE="apt-get ${APT_FLAGS_COMMON} update"  
ARG APTUPGRADE="apt-get ${APT_FLAGS_PERSISTANT} upgrade"  
ARG APTAUTOREMOVE="apt-get ${APT_FLAGS_COMMON} autoremove"  
ARG APTCLEAN="apt-get ${APT_FLAGS_COMMON} clean"  
ARG DELTEMP="rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*"  
ARG APTINSTALL="apt-get ${APT_FLAGS_PERSISTANT} install"  
ARG APTREMOVE="apt-get ${APT_FLAGS_COMMON} purge"  
ARG PIPINSTALL="pip install --no-cache-dir --upgrade"  
ARG PYTHONVER=python3.4  
ENV PYTHONPATH="${PYTHONPATH}/usr/local/lib/${PYTHONVER}/site-packages" \  
IDIOM=es_ES CN=es TZ="Europe/Madrid" \  
DEBIAN_FRONTEND=noninteractive  
  
COPY entrypoint/entry-point.sh .  
RUN $APTUPDATE && $APTUPGRADE && \  
$APTINSTALL gcc \  
linux-headers-amd64 \  
musl-dev \  
ca-certificates \  
openssl \  
python3-setuptools \  
python3-dev \  
git && \  
$PIPINSTALL telepot psutil matplotlib && \  
git clone https://github.com/geekbeard/ServerStatsBot.git /usr/local/src && \  
$DELTEMP  
  
ENTRYPOINT ["/entry-point.sh"]  
CMD ["python3", "/usr/local/src/servstatsbot.py"]  

