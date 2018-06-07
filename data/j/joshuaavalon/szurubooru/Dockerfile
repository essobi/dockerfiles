FROM python:3.6-jessie  
  
ENV PUID=9999 \  
PGID=9999  
VOLUME ["/data"]  
  
ADD run.sh /run.sh  
  
RUN echo "deb http://deb.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt install -y ffmpeg nodejs && \  
git clone https://github.com/rr-/szurubooru.git /szurubooru && \  
chmod +x /run.sh  
  
WORKDIR /szurubooru/client  
  
RUN npm install  
  
WORKDIR /szurubooru/server  
  
RUN pip3 install --no-cache-dir -r requirements.txt && \  
pip3 install --no-cache-dir waitress  
  
ENTRYPOINT ["sh", "/run.sh"]

