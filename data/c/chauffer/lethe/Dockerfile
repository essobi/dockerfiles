FROM node:alpine  
  
ENV DOCKERIZE_VERSION=v0.3.0 \  
LETHE_YOUTUBE_APIKEY="" \  
LETHE_MAX_LENGTH=-1 \  
LETHE_USER_QUEUE_LIMIT=-1 \  
LETHE_TIME_OFFSET=8000 \  
LETHE_DISCORD_ADMIN_ARRAY=""  
RUN apk --no-cache add --virtual=.run-deps ffmpeg && \  
apk --no-cache add --virtual=.build-deps git python build-base wget tar && \  
wget -q -O-
https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-
alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz | tar -zxvf - -C /bin && \  
git clone https://github.com/meew0/Lethe.git /app/ && \  
cd /app && \  
rm -rf .git && \  
npm install && \  
apk del .build-deps  
  
COPY . /app  
WORKDIR /app  
  
CMD ["dockerize", "-template", "lethe-auth.json.tmpl:lethe-auth.json",
"-template", "lethe-config.json.tmpl:lethe-config.json", "node", "lethe.js"]  

