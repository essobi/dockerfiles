FROM node:carbon  
  
COPY . /server-app/  
  
RUN cd /server-app && \  
npm install && \  
npm test && \  
npm run build  
  
EXPOSE 8000  
CMD cd /server-app \  
&& npm run start-build-watch  

