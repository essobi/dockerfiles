# Prod Dockerfile  
FROM node:6  
RUN mkdir /src  
WORKDIR /src  
  
COPY ./ /src  
  
RUN npm install --silent  
RUN node node_modules/.bin/webpack  
  
ENV NODE_ENV production  
  
EXPOSE 3000  
CMD ["node", "bin/www"]  

