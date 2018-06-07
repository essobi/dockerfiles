FROM phusion/passenger-nodejs:latest  
  
RUN apt-get update  
RUN npm cache clean -f && npm install -g n && n 0.10.35  
RUN curl https://install.meteor.com/ | sh  
RUN npm install --silent -g forever  
  
ADD . ./meteorsrc  
WORKDIR /meteorsrc  
  
RUN meteor build --directory .  
RUN cd bundle/programs/server && npm install  
  
WORKDIR /meteorsrc/bundle/  
ENV PORT 5000  
EXPOSE 5000  
RUN touch .foreverignore  
CMD forever --minUptime 1000 --spinSleepTime 1000 -w ./main.js

