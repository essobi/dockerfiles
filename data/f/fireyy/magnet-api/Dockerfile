FROM fireyy/docker-puppeteer:latest  
  
WORKDIR /app  
COPY package.json .  
COPY yarn.lock .  
RUN yarn install --pure-lockfile  
COPY . .  
RUN ls -lA  
EXPOSE 3000  
CMD npm start  

