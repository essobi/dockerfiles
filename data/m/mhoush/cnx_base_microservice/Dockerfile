FROM mhoush/connexion  
  
ADD . /app  
COPY install.sh /install.sh  
  
# Set to 1 or true for debug  
ENV DEBUG=false  
  
WORKDIR /app  
  
CMD ["/usr/local/bin/uwsgi", "--yaml", "config/uwsgi.yml"]  

