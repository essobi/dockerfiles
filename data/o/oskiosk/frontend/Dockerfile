FROM alpine:latest  
  
# Version of the Oskiosk client to Install  
ENV client_version 1.0.16  
# Install dependencies  
RUN apk --no-cache add nginx ca-certificates wget  
  
# Directory where the frontend/client code is stored  
RUN mkdir /oskiosk-client  
WORKDIR /oskiosk-client  
  
# Get the client code  
RUN update-ca-certificates && \  
wget https://github.com/kif-ev/oskiosk-
client/releases/download/$client_version/oskiosk-client.tar.gz && \  
tar xvzf oskiosk-client.tar.gz  
  
# Add config  
ADD nginx.conf /nginx.conf  
RUN mkdir /run/nginx  
  
# Start script  
EXPOSE 8000  
CMD nginx -c /nginx.conf  

