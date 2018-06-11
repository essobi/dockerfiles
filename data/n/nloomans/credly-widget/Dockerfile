FROM node:6.10  
  
WORKDIR /app  
  
ADD . /app  
  
RUN npm run setup  
  
EXPOSE 80  
  
ENV PORT 80  
  
CMD ["npm", "start"]  

