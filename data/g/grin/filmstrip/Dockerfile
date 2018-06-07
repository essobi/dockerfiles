FROM node:latest  
LABEL maintainer "And Grin <a@grin.ly>"  
  
# install npm packages in a separate layer to improve caching  
COPY package*.json /app/  
RUN cd /app && npm set progress=false && npm install  
  
WORKDIR /app  
COPY . /app  
  
ENV PORT=8080  
EXPOSE 8080  
CMD [ "node", "index"]

