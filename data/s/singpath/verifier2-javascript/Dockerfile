FROM node:4.2-slim  
  
RUN mkdir -p /app && \  
adduser --system verifier  
  
WORKDIR /app  
COPY package.json /app/  
RUN npm install  
  
COPY src /app/src  
COPY bin /app/bin  
COPY test /app/test  
COPY .eslintrc .jscsrc /app/  
RUN chmod +x /app/bin/verify && \  
chmod +x /app/src/_runner.js  
  
USER verifier  
ENV PATH="$PATH:/app/bin"  

