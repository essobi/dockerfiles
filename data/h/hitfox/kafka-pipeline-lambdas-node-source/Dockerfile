FROM alpine:edge  
  
# install node dependencies  
RUN apk add --no-cache --update make cmake gcc g++ python git nodejs  
  
# Provide App data  
RUN mkdir -p /app  
WORKDIR /app  
COPY ./package.json /app/package.json  
RUN npm install  
  
# Copy the main application.  
COPY . ./  
  
CMD ["npm", "start"]  

