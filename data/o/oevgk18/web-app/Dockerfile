FROM node:9-alpine  
COPY . /app  
WORKDIR /app  
RUN npm install  
RUN npm run build  
  
FROM node:9-alpine  
RUN npm install -g serve  
COPY \--from=0 /app/build /app  
WORKDIR /app  
CMD ["serve", "-l", "8080", "."]

