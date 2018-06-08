FROM node:4.2.3-wheezy  
ADD . /twitter-bot  
WORKDIR /twitter-bot  
RUN npm install  
RUN mkdir /var/somewhere2  
RUN echo `ls /var/somewhere2`  
ADD . /var/somewhere2  
CMD ["npm", "start"]  

