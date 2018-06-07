FROM node:carbon  
WORKDIR /usr/src/app  
COPY package*.json ./  
COPY yarn.lock ./  
RUN yarn  
COPY . .  
RUN yarn global add prisma  
RUN prisma deploy  
EXPOSE 4000  
CMD ["node", "src"]  

