FROM node:latest  
RUN apt-get update && apt-get install -y unzip  
ADD https://github.com/CookingQuest/koa/archive/master.zip /repo/repo.zip  
WORKDIR /repo  
RUN unzip repo.zip && rm -f repo.zip  
WORKDIR /repo/koa-master  
ENV NODE_ENV=prod  
RUN yarn && yarn run build  
EXPOSE 3001  
CMD ["node", "dist/lib/index.js"]

