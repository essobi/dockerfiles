FROM mhart/alpine-node:7  
# appDir is where we put our code  
ENV appDir /var/www/app/current  
RUN mkdir -p /var/www/app/current  
WORKDIR ${appDir}  
  
# Add package.json to install dependencies  
ADD package.json ./  
  
RUN npm i --production  
RUN npm i -g pm2  
  
ADD . /var/www/app/current  
RUN npm run build:dist  
  
EXPOSE 4500  
CMD ["pm2", "start", "processes.json", "--no-daemon"]  

