FROM nginx:latest  
#build from ubuntu to give the best support for adding modules  
LABEL maintainer="Fivestars Docker Maintainer <docker-maint@fivestars.com>"  
  
# build additional modules  
# copy configs  
COPY configs/conf.d /etc/nginx/conf.d  
COPY configs/nginx.conf /etc/nginx/nginx.conf  
  
#update entry point to map environment variables  

