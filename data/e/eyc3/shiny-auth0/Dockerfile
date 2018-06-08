FROM node:alpine  
  
WORKDIR /app  
  
COPY app/package*.json .  
  
RUN npm install  
  
COPY app/. .  
  
ENV AUTH0_CALLBACK_URL=localhost/callback \  
SHINY_HOST=localhost \  
SHINY_PORT=3838 \  
PORT=3000  
EXPOSE $PORT  
  
CMD ["npm", "start"]

