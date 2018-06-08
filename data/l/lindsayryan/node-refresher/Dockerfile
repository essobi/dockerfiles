FROM lindsayryan/repo-refresher:latest  
  
#Copies node:alpine plus npm  
RUN apk add --update \  
bash \  
nodejs \  
nodejs-npm \  
&& npm install npm@latest -g  
  
ADD node-runner node-runner  
RUN chmod +x node-runner  
RUN /bin/bash -c './node-runner' #this schedules a cron to look for repo and
start app once it's there  
  
ENV UI_DIR=/html  
ENV NODE_DIR=/services  
ENV PORT=80  
EXPOSE 8080 433 $PORT  
  

