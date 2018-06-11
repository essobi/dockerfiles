FROM nginx:alpine  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY ./dist /usr/src/app/  
  
COPY nginx.conf /etc/nginx/nginx.conf  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
EXPOSE 80  
# Set the default command to execute  
# when creating a new container  
CMD ["nginx"]  

