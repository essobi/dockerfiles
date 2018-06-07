FROM node:6.3  
MAINTAINER Mees van Dijk  
  
RUN mkdir -p /usr/app  
WORKDIR /usr/app  
  
RUN git clone https://github.com/mees-/listie.git .  
RUN npm install  
RUN npm install -g grunt-cli  
RUN grunt build  
  
ENV PORT 8080  
EXPOSE 8080  
CMD ["npm","start"]  

