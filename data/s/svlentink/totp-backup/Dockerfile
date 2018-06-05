FROM node:alpine  
  
RUN mkdir /app  
WORKDIR /app  
RUN npm install qrcode-terminal prompt speakeasy  
  
# in/output file  
VOLUME /storage  
ENV SECRETSFILE /storage/secrets.json  
  
ENTRYPOINT ["node","/app/main.js"]  
COPY main.js /app/  

