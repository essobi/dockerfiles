FROM node  
  
MAINTAINER colhom@gmail.com  
  
ADD ./package.json /usr/src/marbel/package.json  
  
WORKDIR /usr/src/marbel  
RUN npm install -g nodemon  
RUN npm install . -g  
  
ADD . /usr/src/marbel  
  
ENV NODE_PATH /usr/local/lib/node_modules/marvel/node_modules/  
  
ENTRYPOINT ["node"]  
  
EXPOSE 8765  

