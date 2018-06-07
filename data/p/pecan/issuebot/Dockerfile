FROM node:alpine  
  
env HUBOT_SLACK_TOKEN="" \  
HUBOT_GITHUB_TOKEN=""  
WORKDIR /bot  
COPY package.json /bot/  
RUN npm install  
COPY . /bot/  
  
ENTRYPOINT ["./entrypoint.sh"]  
CMD ["bot"]  

