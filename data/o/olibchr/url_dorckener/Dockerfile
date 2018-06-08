FROM zerotier/zerotier-containerized:latest  
  
# Update  
RUN apk add --update python py-pip  
  
# Copy the application folder inside the container  
ADD / /url_shortener/  
  
## Socat  
RUN apk add --no-cache socat  
EXPOSE 5000  
# Join network during runtime  
# RUN /zerotier-cli join a09acf0233195342  

