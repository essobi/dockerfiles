FROM node:9.11.1  
ENV PORT 80  
ENV CACHE_BACKEND http://backend/  
EXPOSE 80  
COPY package.json /app/  
WORKDIR /app  
  
RUN npm set progress=false  
RUN npm install  
  
COPY *.js /app/  
  
CMD ["npm", "run", "start"]  

