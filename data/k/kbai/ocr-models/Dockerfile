# Build:  
# docker build -t kbai/ocr-models .  
# Run:  
# docker run --restart=on-failure --rm -it -p 3002:3002 kbai/ocr-models  
FROM node:argon  
  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY package.json /app/  
RUN npm install  
  
COPY . .  
  
EXPOSE 3002  
CMD npm start  

