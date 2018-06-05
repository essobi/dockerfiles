FROM node:argon  
MAINTAINER Jared Dickson <code@jareddickson.com>  
  
# Update npm to 3.x latest and then install Bower and Gulp  
RUN npm install -g npm@3 \  
&& npm install -g bower gulp \  
&& npm cache clean  
  
CMD ["bash"]  

