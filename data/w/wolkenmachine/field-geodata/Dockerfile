FROM node:argon  
  
#Environment Variables  
ENV DATABASE_URI redis://redis  
  
# Create app directory  
RUN mkdir -p /app  
WORKDIR /app  
  
# Install  
COPY package.json /app  
COPY main.js /app  
  
COPY config.docker.js /app/config.js  
  
# Bundle  
RUN npm install  
  
#Image configuration  
ADD start.sh /start.sh  
RUN chmod 755 /*.sh  
  
EXPOSE 80  
CMD ["/start.sh"]  

