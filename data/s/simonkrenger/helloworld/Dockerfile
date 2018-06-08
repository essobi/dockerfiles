FROM python:3-slim  
MAINTAINER Simon Krenger <simon@krenger.ch>  
  
COPY index.html /var/www/index.html  
  
WORKDIR /var/www/  
  
EXPOSE 80  
CMD [ "python3", "-u", "-m", "http.server", "80" ]  

