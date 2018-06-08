FROM node:8  
RUN apt-get update  
#RUN npm install pm2@next -g  
WORKDIR /app/nodebot  
ADD . /app/nodebot  
RUN npm install  
## DEVELOPMENT MODE  
# ENV NODE_ENV=development  
ENTRYPOINT ["node"]  
CMD [ "/app/nodebot/bot.js" ]  

