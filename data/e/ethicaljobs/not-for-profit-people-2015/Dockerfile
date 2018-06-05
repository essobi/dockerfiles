FROM andrewmclagan/aphex:latest  
  
#  
#--------------------------------------------------------------------------  
# Application  
#--------------------------------------------------------------------------  
#  
ADD ./config/nginx.conf /etc/nginx/nginx.conf  
  
ADD ./config/entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
RUN mkdir -p /var/www  
  
WORKDIR /var/www  
  
ADD . /var/www  
  
#  
#--------------------------------------------------------------------------  
# Init  
#--------------------------------------------------------------------------  
#  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD /usr/bin/supervisord

