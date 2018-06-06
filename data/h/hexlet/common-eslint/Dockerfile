FROM node:9.9.0  
WORKDIR /linter  
  
COPY package.json /linter  
RUN npm install  
  
COPY linter linter  
RUN chmod +x linter  
  
VOLUME /tmp  
  
CMD ./linter  

