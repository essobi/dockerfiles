FROM mhart/alpine-node:5.9  
# Provide App data  
RUN npm install forever -g  
RUN mkdir -p /app  
WORKDIR /app  
COPY ./package.json /app/package.json  
RUN npm install  
  
# Copy the main application.  
COPY . ./  
  
CMD ["npm", "start"]  

