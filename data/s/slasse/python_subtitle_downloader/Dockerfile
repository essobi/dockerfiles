FROM ubuntu:latest  
MAINTAINER Slasse <ladislas.kiekens@telenet.be>  
  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
python \  
cron \  
wget \  
vim \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN useradd -ms /bin/bash localadm  
ADD crontab /etc/cron.d/subtitles-cron  
RUN chmod 0644 /etc/cron.d/subtitles-cron  
RUN mkdir -p /opt/subtitle_downloader/logs && mkdir /movies && touch
/opt/subtitle_downloader/logs/cron_new.log  
COPY ./OpenSubtitlesDownload.py /opt/subtitle_downloader  
COPY ./main.py /opt/subtitle_downloader  
RUN chown -R localadm /opt/subtitle_downloader  
  
VOLUME ["/opt/subtitle_downloader/logs","/movies"]  
  
CMD cron && tail -f /opt/subtitle_downloader/logs/cron_new.log

