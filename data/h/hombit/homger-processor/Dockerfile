FROM hombit/homger  
  
  
MAINTAINER Konstantin Malanchev "hombit@gmail.com"  
  
  
# Calibre  
RUN apt-get -y install python2.7 python-imaging python-qt4 python-mechanize
imagemagick xdg-utils python-lxml python-dateutil python-cssutils python-
beautifulsoup python-dnspython poppler-utils libpodofo libwmf0.2-7 libicu52
libmtp9 python-netifaces python-psutil python-cssselect python-apsw  
  
RUN apt-get -y install wget tar xz-utils  
  
RUN wget -nv -O- https://github.com/kovidgoyal/calibre/raw/master/setup/linux-
installer.py | sudo python -c "import sys;
main=lambda:sys.stderr.write('Download failed\n'); exec(sys.stdin.read());
main()"  
  
  
# Convert tools:  
RUN apt-get install --yes \  
unoconv \  
ghostscript \  
djvulibre-bin \  
atool unrar-free lzma p7zip lbzip2 plzip lzop  
  
  
# Start processor  
CMD ./processor.py  

