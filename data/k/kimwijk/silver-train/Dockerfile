FROM mhart/alpine-node:8.9.4  
WORKDIR /src  
ADD . .  
  
RUN npm install  
RUN npm run build  
  
ENV PORT 3000  
EXPOSE $PORT  
  
CMD ["npm", "run", "start:prod"]  

