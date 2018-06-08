FROM node:8  
COPY ./app /usr/src/app  
  
RUN cd /usr/src/app && \  
npm install  
  
RUN cd /usr/src/app/gui && \  
npm install && \  
npm run build-app  
  
EXPOSE 80  
EXPOSE 4580  
WORKDIR /usr/src/app  
  
CMD ["node", "app.js"]  

