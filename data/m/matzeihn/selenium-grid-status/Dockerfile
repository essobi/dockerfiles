FROM node  
  
RUN npm install express selenium-grid-status  
COPY webapp.js /webapp.js  
  
EXPOSE 4445  
CMD ["localhost","4444"]  
ENTRYPOINT ["node","/webapp.js"]  

