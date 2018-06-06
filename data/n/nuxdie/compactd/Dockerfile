FROM node:8.11.1  
WORKDIR /app  
  
ADD . .  
  
RUN npm i  
  
EXPOSE 80  
CMD ["compactd", "--serve"]  

