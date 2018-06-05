FROM node:6.9.4  
  
RUN apt-get update \  
&& apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 \  
&& echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.2.list \  
&& apt-get update \  
&& apt-get install -y mongodb-org \  
&& npm install -g yarn \  
&& npm install -g pm2  

