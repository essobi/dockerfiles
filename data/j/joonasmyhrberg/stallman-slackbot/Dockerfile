FROM mhart/alpine-node  
  
RUN mkdir /src  
WORKDIR /src  
  
ADD rms-bot.js /src/rms-bot.js  
ADD package.json /src/package.json  
  
RUN npm install  
  
CMD ["node","rms-bot.js"]  

