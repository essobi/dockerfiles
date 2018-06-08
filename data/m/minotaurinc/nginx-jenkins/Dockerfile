FROM nginx  
  
RUN rm /etc/nginx/conf.d/default.conf  
  
COPY files/conf.d/jenkins.conf /etc/nginx/conf.d/jenkins.conf  
COPY files/nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 80  
EXPOSE 443  

