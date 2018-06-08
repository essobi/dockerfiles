FROM node:9.3.0  
COPY . .  
RUN npm install -g typescript  
RUN npm install  
RUN tsc  
EXPOSE 8080  
CMD ["node", "./SpongebobMockeryBot.js"]

