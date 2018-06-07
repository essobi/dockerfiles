FROM python:2-slim  
  
WORKDIR /app  
  
RUN echo "deb http://www.deb-multimedia.org jessie main non-free" >
/etc/apt/sources.list.d/multimedia.list && \  
apt-get update && \  
apt-get install -y -q --force-yes --no-install-recommends ffmpeg mpg123
vorbis-tools lame flac build-essential && \  
pip install flask storm pillow simplejson requests mutagen watchdog gunicorn
https://github.com/spl0k/supysonic/archive/master.tar.gz && \  
mkdir /data && \  
apt-get remove -y -q build-essential && \  
apt-get autoremove -y -q && \  
rm -rf /var/lib/apt/lists/*  
  
USER ${PUID:-1001}  
COPY app.py /app/app.py  
COPY supysonic.conf /etc/supysonic  
COPY docker-entrypoint.sh /  
  
VOLUME ["/data", "/music"]  
EXPOSE 8000  
ENTRYPOINT ["/docker-entrypoint.sh"]

