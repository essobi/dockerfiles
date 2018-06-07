FROM node:argon  
  
# Create app directory  
RUN mkdir -p /app  
WORKDIR /app  
  
# Install  
COPY package.json /app  
COPY main.js /app  
COPY ./static /app/static  
  
# Bundle  
RUN npm install  
  
EXPOSE 80  
CMD ["node","main.js"]  

