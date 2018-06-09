FROM lsiobase/xenial  
  
MAINTAINER ccridge <cl.mail.forwarding@gmail.com>  
# Based on the work of Eric Schultz <eric@startuperic.com> and needo
<needo@superhero.org>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install python and encoder tools  
RUN apt-get update && apt-get install -y --force-yes ffmpeg python-pyudev wget
cron  
RUN apt-get clean  
  
# Bring in our config and data files path  
VOLUME ["/data"]  
VOLUME ["/config"]  
VOLUME ["/transcode"]  
  
# add local files  
COPY root/ /  
  
RUN chmod +x /etc/cron.hourly/cpFromTablo \  
/defaults/config/scripts/cpFromTablo.py \  
/usr/local/bin/ccextractor  

