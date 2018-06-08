FROM nginx  
MAINTAINER henrik@hedlund.im  
  
# Create the new HTML root directory  
RUN mkdir /app  
  
# Set nginx to use the the new directory  
RUN sed -i 's|/usr/share/nginx/html|/app|g' /etc/nginx/conf.d/default.conf  
  
# Disable caching  
RUN sed -i 's/server_name localhost;/server_name localhost;\n sendfile off;/g'
/etc/nginx/conf.d/default.conf  
  
# Map the HTML root as a volume  
VOLUME [ "/app" ]  
  

