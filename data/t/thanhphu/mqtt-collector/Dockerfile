FROM node:6  
LABEL maintainer="Thanh Phu <nvtphu+docker@gmail.com>"  
  
WORKDIR /app  
COPY package.json /app  
RUN npm install  
COPY . /app  
  
CMD ["npm", "start"]

