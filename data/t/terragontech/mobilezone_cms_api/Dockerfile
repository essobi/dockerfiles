FROM terragontech/node:6.9  
RUN mkdir -p /usr/src/app  
RUN mkdir -p /usr/src/app/uploads  
RUN mkdir -p /usr/src/app/uploads/crbt  
RUN mkdir -p /usr/src/app/uploads/sms  
RUN mkdir -p /usr/src/app/uploads/game  
RUN mkdir -p /usr/src/app/uploads/video  
RUN mkdir -p /usr/src/app/uploads/category  
RUN mkdir -p /usr/src/app/uploads/partner  
RUN mkdir -p /usr/src/app/uploads/games  
RUN mkdir -p /usr/src/app/uploads/main_arts  
RUN mkdir -p /usr/src/app/uploads/games_screenshots  
WORKDIR /usr/src/app  
COPY package.json /usr/src/app/  
RUN npm install && npm cache clean  
COPY . /usr/src/app  
EXPOSE 1003  
CMD ["npm","start"]

