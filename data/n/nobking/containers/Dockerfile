#joe practice  
FROM google/nodejs  
MAINTAINER yeah boyyy  
  
WORKDIR /home  
RUN git clone https://github.com/shrikrishnaholla/code.it.git  
  
WORKDIR code.it  
RUN git submodule update --init --recursive  
RUN npm install  
  
EXPOSE 8000  
WORKDIR /home  
CMD ["node", "/home/code.it/app.js"]  

