FROM nginx  
  
MAINTAINER Mackilem Van der Laan <comercial@trustcode.com.br> \  
Danimar Ribeiro <desenvolvimento@trustcode.com.br>  
  
  
WORKDIR /etc/nginx/  
RUN mkdir sites-enabled  
ADD conf/nginx.conf /etc/nginx/  
RUN rm /etc/nginx/conf.d/default.conf  
  
CMD ["nginx", "-g", "daemon off;"]  

