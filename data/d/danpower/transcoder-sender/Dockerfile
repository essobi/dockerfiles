FROM node  
  
MAINTAINER Dan Power  
  
ENV RABBITMQ=rabbitmq \  
WATCH_PATH="/mnt/media" \  
TRANSCODE_FROM="avi" \  
HANDBRAKE_OPTS="{encoder:'x264',quality:22,rate:25,ab:64,maxWidth:480,optimize:true}"  
LABEL project="au.id.danpower.transcoder" version=1.0  
  
VOLUME $WATCH_PATH  
  
RUN git clone https://github.com/dan-power/transcoder-sender.git
/var/transcoder-sender && \  
cd /var/transcoder-sender && \  
npm install  
  
CMD ["node", "/var/transcoder-sender/sender.js"]  

