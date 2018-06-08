FROM node  
  
MAINTAINER vincent.aceto@gmail.com  
  
RUN git clone -q https://github.com/vinnyA3/url-shortener-microservice.git  
  
# Update repo sources list  
RUN apt-get update  
  
# Use microservice sub dir as image work dir  
WORKDIR url-shortener-microservice/microservice  
  
RUN yarn install > /dev/null  
  
EXPOSE 8080  
CMD ["npm", "start"]  

