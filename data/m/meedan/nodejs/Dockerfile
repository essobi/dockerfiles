# meedan/nodejs  
FROM meedan/base  
MAINTAINER sysops@meedan.com  
  
# nodejs repo  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
RUN apt-get install -y \  
nodejs  
  
RUN npm install -g \  
nodemon \  
pm2 \  
node-static \  
bower \  
gulp

