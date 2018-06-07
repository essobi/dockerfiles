FROM node:6-slim  
  
ENV INTERFACE=0.0.0.0 PORT=80 FORWARD=localhost:80 DUPLICATE=localhost:8080  
  
RUN npm install -g duplicator  
  
CMD duplicator -f $FORWARD -d $DUPLICATE -p $PORT -i $INTERFACE  

