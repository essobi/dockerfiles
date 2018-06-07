FROM nginx  
  
RUN apt-get update  
RUN apt-get install -y python3  
  
RUN mkdir /etc/nginx/certs  
RUN mkdir /etc/nginx/clients  
  
COPY nginx/etc /etc/nginx/  
COPY nginx/html /usr/share/nginx/html/  
  
CMD ["python3", "/etc/nginx/app-wrapper.py", "/etc/nginx/app-wrapper-
config.json"]

