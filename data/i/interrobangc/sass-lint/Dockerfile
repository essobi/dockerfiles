FROM node:alpine  
  
RUN npm install -g sass-lint  
  
WORKDIR /app  
  
CMD ["sass-lint", "-v", "-q", "--max-warnings", "0"]  

