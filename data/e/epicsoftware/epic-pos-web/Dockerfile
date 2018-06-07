FROM node:6.9.5  
ADD . /app  
WORKDIR /app  
  
# Install app dependencies  
ADD package.json /app/package.json  
RUN npm install  
CMD npm start  
  
EXPOSE 3000  
ENV PORT=3000  
ENV BASE_URL="https://0.0.0.0"

