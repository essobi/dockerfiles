FROM debian:stable  
  
MAINTAINER YuLun Shih <shih@yulun.me>  
  
ADD https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-
installer.py /scripts/  
  
RUN apt-get update && \  
apt-get install -y curl xvfb python xdg-utils imagemagick \  
python-imaging python-mechanize python-lxml python-dateutil \  
python-cssutils python-beautifulsoup python-dnspython python-poppler \  
libpodofo-utils libwmf-bin python-chm && \  
python /scripts/linux-installer.py  
  
COPY . /data  
  
VOLUME ["/data/output"]  
  
CMD /data/throw.sh

