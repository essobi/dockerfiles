# Version 0.1.1  
FROM dockerfile/nodejs  
MAINTAINER Shrikrishna Holla  
  
RUN git clone https://github.com/pesos/optimus.git /home/optimus  
WORKDIR /home/optimus  
RUN npm install  
  
CMD ["/usr/local/bin/npm", "start"]  

