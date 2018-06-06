FROM node:9.5.0-alpine AS base  
RUN apk add --no-cache git && \  
git clone https://github.com/volpe28v/DevHub && \  
cd DevHub && \  
git checkout 64f551f1f58e886a6b581658a311787c5d082930 && \  
npm install && \  
npm run build  
  
FROM base AS release  
RUN apk add --no-cache tzdata  
  
COPY \--from=base /DevHub /DevHub  
WORKDIR /DevHub  
EXPOSE 3000  
ENTRYPOINT ["npm","start","--"]  

