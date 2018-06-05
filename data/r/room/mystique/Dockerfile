FROM node  
MAINTAINER Harrison Shoebridge <harrison@theshoebridges.com>  
  
RUN git clone https://github.com/bigroom/mystique.git /app  
  
RUN npm install -g bower http-server  
  
WORKDIR /app  
  
RUN bower install --allow-root  
  
CMD http-server /app/src  

