## @project : Spire Engineering website  
## @about : Basic HTML website run on Nginx.  
  
# Base Docker image  
FROM nginx:1  
  
# Maintainer  
MAINTAINER support@vieo.co  
  
# Set container environment variables  
ENV NGINX_ENV=production  
ENV PORT=8080  
  
# Copy source code and content  
COPY . /usr/share/nginx/html  
  
# Execute Install time commands  
#RUN cd /  
  
# Expose container port  
EXPOSE $PORT  

