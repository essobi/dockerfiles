FROM nginx:latest  
MAINTAINER i_am_nutt@hotmail.com  
  
# Copy index.html  
COPY index.html /usr/share/nginx/html/  
  
# make directory for javascript  
RUN mkdir -p /usr/share/nginx/html/build  
  
# Copy javascript files  
COPY build/ /usr/share/nginx/html/build/  
  
RUN chmod -R 755 /usr/share/nginx/html/  
RUN ls -la /usr/share/nginx/html/build/  
  
# expose port 80  
EXPOSE 80  

