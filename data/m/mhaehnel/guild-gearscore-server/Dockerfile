FROM node:8-alpine  
  
ENV NODE_ENV=production  
ENV HOST=0.0.0.0  
ENV PORT=3000  
ENV CORS=true  
  
# Create app directory  
WORKDIR /app  
COPY . /app  
  
RUN yarn install  
  
EXPOSE 3000  
CMD [ "yarn", "start" ]  

