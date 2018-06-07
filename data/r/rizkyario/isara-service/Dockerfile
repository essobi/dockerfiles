# docker build -t rizkyario/incubator:beta .  
#Choose a base image  
FROM node:6.3.1-slim  
  
# Create a new folder for our application  
RUN mkdir -p /var/www/  
  
# Define working directory  
WORKDIR /var/www/  
  
ADD . /var/www/  
  
# Install PM2  
RUN npm install -g pm2  
# RUN npm install -g yarn  
# Install our packages  
# RUN yarn  
RUN npm install  
  
#Expose our application port  
EXPOSE 3000:80  
RUN chmod a+x /var/www/docker-start.sh  
  
# Set start command  
CMD bash docker-start.sh

