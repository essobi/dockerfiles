FROM node:carbon  
  
## Check out latest source code from the git  
WORKDIR /usr/src/app  
  
COPY package*.json ./  
  
RUN npm install  
RUN npm install -g serve@6.4.11  
  
COPY . .  
  
EXPOSE 5000  
## Remove stack docker from the dir  
CMD ["sh", "frontend.sh"]  

