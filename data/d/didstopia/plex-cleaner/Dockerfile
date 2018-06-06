FROM didstopia/base:alpine-3.5  
  
MAINTAINER Didstopia <support@didstopia.com>  
  
# Plex Cleaner URL  
ENV PLEX_CLEANER_URL="https://github.com/ngovil21/Plex-
Cleaner/archive/9797292b55ea1e0720d40d38cfb16818aed3d2f8.zip"  
# Use root user by default  
USER root  
  
# Install dependencies  
RUN apk --no-cache add \  
busybox-suid \  
unzip \  
python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
rm -r /root/.cache  
  
# Ensure Python was correctly installed  
RUN python3 --version  
  
# Setup default user  
RUN addgroup -g 1000 plexcleaner && \  
adduser -u 1000 -G plexcleaner -s /bin/sh -D plexcleaner  
  
# Install Plex Cleaner  
ADD ${PLEX_CLEANER_URL} /tmp/plexcleaner.zip  
RUN mkdir -p /plexcleaner && \  
unzip -j /tmp/plexcleaner.zip -d /plexcleaner && \  
chown -R plexcleaner:plexcleaner /plexcleaner && \  
rm -f /tmp/plexcleaner.zip  
  
# Setup scheduled running of Plex Cleaner  
COPY plexcleaner.cron /tmp/plexcleaner.cron  
RUN crontab -u plexcleaner /tmp/plexcleaner.cron  
  
# Setup volumes  
RUN mkdir -p /config && \  
chown -R plexcleaner:plexcleaner /config  
VOLUME /config  
  
# Set the entry point  
ENTRYPOINT crond -fS  

