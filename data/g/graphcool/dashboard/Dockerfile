FROM mhart/alpine-node  
  
RUN apk add --update git build-base python  
  
COPY . /app  
WORKDIR /app  
  
RUN npm install  
  
RUN apk del git build-base python  
  
ENV BACKEND_ADDR **None**  
ENV DASHBOARD_SCHEMA_ENDPOINT **None**  
  
EXPOSE 4000  
CMD ["npm", "start"]  

