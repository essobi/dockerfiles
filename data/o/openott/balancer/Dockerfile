FROM nginx  
MAINTAINER Viknet <viknet@icloud.com>  
  
RUN mkdir /app/  
  
COPY clientaccesspolicy.xml /var/www/  
COPY crossdomain.xml /var/www/  
COPY nginx.conf /data/template  
COPY Procfile /app/  
  
COPY consul-template /app/  
COPY forego /app/  
COPY entrypoint.sh /app/  
  
WORKDIR /app/  
  
ENTRYPOINT ["/app/forego", "start", "-r"]  

