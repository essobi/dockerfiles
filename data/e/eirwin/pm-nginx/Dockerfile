FROM nginx  
  
RUN apt-get update && apt-get install -y \  
nano  
  
RUN mkdir /etc/nginx/sites-available  
RUN mkdir /etc/nginx/sites-enabled  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
COPY sites-available/app /etc/nginx/sites-available/app  
COPY sites-available/site /etc/nginx/sites-available/site  
  
RUN ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app  
RUN ln -s /etc/nginx/sites-available/site /etc/nginx/sites-enabled/site  

