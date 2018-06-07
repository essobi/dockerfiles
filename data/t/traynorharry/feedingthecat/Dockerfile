############################################################  
#  
# 0.0.1  
#  
# - BUILD -  
# docker build --no-cache -t traynorharry/feedingthe.cat-www:0.0.* .  
#  
# - RUN PREREQ -  
# docker run -d -p 32770:3306 -e MYSQL_ROOT_PASSWORD=12345678 \--name ftcDB
mysql:8.0.1  
#  
# - RUN -  
# docker pull index.docker.io/traynorharry/feedingthe.cat-www:latest  
# docker run -d -p 443:3000 -p 80:3000 \--name ftcWWW
index.docker.io/traynorharry/feedingthe.cat-www:latest  
#  
############################################################  
  
FROM node:alpine  
MAINTAINER harry@sb2.team  
  
##################### GENERAL INSTALL #####################  
  
# install git  
RUN apk add --no-cache git  
  
##################### APP INSTALL #####################  
  
# set directory for app  
RUN mkdir -p /usr/src/app  
  
# set working directory  
WORKDIR /usr/src/app  
  
# git clone over https  
RUN git clone --depth=1 -b master
https://ab04f7a7d695210303729fc3130d776b8e3eb0f5@github.com/harrytraynor/feedingthe.cat-
WWW.git  
  
# set working directory to git clone  
WORKDIR /usr/src/app/feedingthe.cat-WWW  
  
# run npm install for node  
RUN npm install --production  
  
##################### INSTALLATION END #####################  
  
# set default port  
EXPOSE 3000 80 443  
  
# set default command to run  
ENTRYPOINT ["npm", "start"]  

