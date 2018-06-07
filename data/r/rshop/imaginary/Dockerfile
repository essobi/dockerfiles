FROM node:8  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY index.js /app/  
COPY package.json /app/  
COPY package-lock.json /app/  
  
RUN apt-get update && apt-get install -y \  
imagemagick \  
jpegoptim \  
gifsicle \  
pngquant  
  
WORKDIR /app  
RUN npm install  
  
EXPOSE 9099  
CMD ["node", "/app/index.js"]  

