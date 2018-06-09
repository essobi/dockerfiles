FROM node:0.12  
WORKDIR /backend  
EXPOSE 3000  
ADD . /backend  
  
RUN rm -rf node_install \  
&& npm install -g nodemon \  
&& npm install  
  
CMD ["node", "index.js"]  

