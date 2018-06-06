FROM node  
  
LABEL maintainer "tom@thomaslorentsen.co.uk"  
  
WORKDIR /home/node/  
  
COPY package.json package.json  
  
RUN yarn  
  
COPY app.js .  
COPY js js  
COPY views views  
  
EXPOSE 4444  
CMD [ "node", "app.js" ]  

