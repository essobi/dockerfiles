FROM node:6-alpine  
  
COPY . /app  
WORKDIR /app  
  
ENV ANSI_COLOR disabled  
  
RUN yarn install --non-interactive && \  
yarn compile && \  
yarn install --production --non-interactive  
  
CMD ["yarn", "start"]  

