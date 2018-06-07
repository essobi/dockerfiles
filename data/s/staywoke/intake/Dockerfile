FROM node:6-onbuild  
RUN echo "PORT=3030" > .env  
  
RUN npm run build  
  
EXPOSE 3030  
ENTRYPOINT ["npm", "run"]  

