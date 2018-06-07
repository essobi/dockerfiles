FROM node  
  
# Copy source  
COPY root/ /  
  
# Make /config and install dependencies  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends ffmpeg && \  
mkdir /config && \  
cd /usr/src/app && \  
npm install discord.js node-opus ffmpeg-binaries simple-tts-docker --save  
  
EXPOSE 8080  
VOLUME /config  
CMD ["/usr/src/run.sh"]  

