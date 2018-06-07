# Use the Latest LTS Ubuntu Version  
FROM honkdev/common:1.0.1  
MAINTAINER HONK Technologies, Inc.  
  
# Copy our nginx config to the right place  
COPY nginx.conf /etc/nginx/nginx.conf  
  
# Port corresponding to the port we set as our upstream app in our nginx.conf  
ENV PORT=5000  
# Set the Working Directory for All Commands that Follow  
WORKDIR /app  
  
COPY start.sh bin/  
  
CMD ['./bin/start.sh']  

