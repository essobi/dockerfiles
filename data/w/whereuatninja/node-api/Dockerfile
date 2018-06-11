FROM node:latest  
  
MAINTAINER whereuat.ninja: info@whereuat.ninja  
  
COPY . /var/www  
WORKDIR /var/www  
  
RUN apt-get update  
  
RUN npm install -g pm2@latest  
  
RUN mkdir -p /var/log/pm2  
  
EXPOSE 3000  
ENTRYPOINT ["pm2", "start", "server.js", "--name", "whereuat-api", "--log",
"/var/log/pm2/pm2.log", "--watch", "--no-daemon"]  
  
# To Build:  
# docker build -f .\docker\node.dockerfile -t whereuatninja/node-api .  
# To Run:  
# docker run -d -p 3000:3000 -e "WHEREUAT_API_APP_ENV=development" --name
node-api whereuatninja/node-api

