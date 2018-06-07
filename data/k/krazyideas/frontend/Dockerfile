FROM node:5.12  
# Create app directory  
RUN mkdir -p /usr/src/myapp  
WORKDIR /usr/src/myapp  
  
RUN cd /usr/src/myapp  
RUN wget https://github.com/krazyideas/frontend/archive/v0.0.4.tar.gz  
RUN tar --strip-component 1 -zxvf v0.0.4.tar.gz  
  
# Satisfy dependencies  
RUN npm install  
  
EXPOSE 3000  
CMD npm start  

