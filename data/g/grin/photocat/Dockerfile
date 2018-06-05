FROM node:alpine  
LABEL maintainer "And Grin <a@grin.ly>"  
  
# install npm packages in a separate layer to improve caching  
COPY package*.json /app/  
RUN cd /app && npm set progress=false && npm install  
  
WORKDIR /app  
COPY . /app  
  
ENV PORT=8081  
EXPOSE 8081  
CMD [ "node", "index"]

