FROM node:8.4.0  
LABEL maintainer "Appverse <publish@appverse.io>"  
RUN npm install -g bower && npm install -g grunt  
RUN apt update && apt install -y ruby ruby-dev && gem update --system && gem
install compass -v 1.0.1 && rm -rf /var/lib/apt/lists/*  

