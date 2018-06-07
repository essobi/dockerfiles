FROM python:2-onbuild  
MAINTAINER Ted Chen <tedlchen@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y cron rsync librsync-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download and install duplicity  
RUN export VERSION=0.6.26 \  
&& cd /tmp/ \  
&& wget
https://code.launchpad.net/duplicity/0.6-series/$VERSION/+download/duplicity-$VERSION.tar.gz
\  
&& cd /opt/ \  
&& tar xzvf /tmp/duplicity-$VERSION.tar.gz \  
&& rm /tmp/duplicity-$VERSION.tar.gz \  
&& cd duplicity-$VERSION \  
&& ./setup.py install \  
&& rm -rf /tmp/* /var/tmp/*  
  
# Exposed environments  
ENV CRON_SCHEDULE="0 1 * * *"  
ENV SOURCE=""  
ENV REMOTE_URL=""  
ENV PARAMS="--full-if-older-than 1M"  
ENV PASSPHRASE=""  
ENV AWS_ACCESS_KEY_ID=""  
ENV AWS_SECRET_ACCESS_KEY=""  
RUN chmod a+x /usr/src/app/*.sh \  
&& ln -s /usr/src/app/backup.sh /usr/local/sbin/backup \  
&& ln -s /usr/src/app/list.sh /usr/local/sbin/list \  
&& ln -s /usr/src/app/restore.sh /usr/local/sbin/restore \  
&& ln -s /usr/src/app/status.sh /usr/local/sbin/status  
  
ENTRYPOINT ["/usr/src/app/start.sh"]  
CMD [""]

