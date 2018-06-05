FROM tozd/cron:ubuntu-xenial  
  
VOLUME /tumblr-backup  
VOLUME /tumblr-backup-history  
  
RUN apt-get update -q -q && \  
apt-get --yes --force-yes install python python-pyexiv2 youtube-dl rdiff-
backup  
  
COPY ./tumblr-utils /tumblr-utils  
  
COPY ./etc /etc  

