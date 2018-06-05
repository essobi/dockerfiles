FROM nginx  
  
MAINTAINER Go About <tech@goabout.com>  
  
# Configure Nginx  
RUN apt-get -qq update && \  
apt-get -qq install openssl && \  
openssl dhparam -out /etc/ssl/dh_2048.pem 2048  
RUN mkdir -p /var/spool/nginx/client_temp  
  
RUN rm /etc/nginx/conf.d/default.conf  
COPY nginx.conf /templates/etc/nginx/nginx.conf  
COPY status.conf /etc/nginx/conf.d/  
  
# Add templating entry point  
ADD https://github.com/jcassee/parameterized-
entrypoint/releases/download/0.9.0/entrypoint_linux_amd64
/usr/local/bin/entrypoint  
RUN chmod +x /usr/local/bin/entrypoint  
  
ENTRYPOINT ["entrypoint", "--"]  
CMD ["nginx"]  

