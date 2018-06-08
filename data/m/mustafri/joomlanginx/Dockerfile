FROM nginx  
# configuration file to add SSL certificates, listen on 443 and proxy requests
to 80  
COPY ./conf/nginx.conf /etc/nginx/nginx.conf  
CMD ["nginx", "-g", "daemon off;"]  
# add certificates  
RUN mkdir /etc/nginx/cert/  
ADD ./cert /etc/nginx/cert/  

