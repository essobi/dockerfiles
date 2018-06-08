FROM node:6.2-onbuild  
ONBUILD RUN npm install --no-optional  
  
VOLUME ["/usr/src/app"]  
  
EXPOSE 80 3000 3001  
CMD ["npm", "start", "--", "--port", "80"]  

