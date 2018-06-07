FROM nodesource/node:trusty  
  
RUN mkdir -p /usr/src/npm  
WORKDIR /usr/src/npm  
  
RUN npm install fis3  
RUN npm install fis3-hook-module  
RUN npm install fis3-postpackager-loader  
RUN npm install fis-parser-less-2.x  
RUN npm install fis-parser-sass  
  
ENV PATH=/usr/src/npm/node_modules/.bin:$PATH  
  
EXPOSE 8080  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
CMD ["bash"]  

