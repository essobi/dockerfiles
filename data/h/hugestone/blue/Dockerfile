FROM node:argon  
  
# work dir  
RUN mkdir -p /app/grosnc  
WORKDIR /app/grosnc  
  
#Dockerfile Maintainer  
MAINTAINER Junho Yoon <yoonjho79@gmail.com>  
  
# get source from git repos  
RUN git clone https://github.com/grosnc/blue ./  
  
#install dependencies lib  
RUN npm install  
  
# expose port  
EXPOSE 3000  
# star command  
CMD ["npm", "start"]  
  

