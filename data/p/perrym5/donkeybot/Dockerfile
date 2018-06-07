FROM node:9  
ADD package.json yarn.lock /bot/  
  
RUN cd /bot && yarn  
  
ADD . /bot/  
  
WORKDIR /bot  
  
ENTRYPOINT ["node", "./bin/donkeybot.js", "--name", "donkeybot", "-a",
"discord", "-l", "db"]  

