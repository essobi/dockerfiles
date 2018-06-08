FROM node:latest  
EXPOSE 8000  
RUN git clone https://github.com/jacomyal/sigma.js.git  
WORKDIR sigma.js  
RUN npm install  
RUN touch index.html  
RUN npm run build  
RUN mkdir /app  
RUN ln -s /app  
CMD ["npm", "start"]  

