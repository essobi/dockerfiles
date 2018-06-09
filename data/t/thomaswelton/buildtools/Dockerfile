FROM thomaswelton/node  
  
MAINTAINER thomaswelton  
  
RUN npm install -g gulp bower  
  
ADD run.sh /run.sh  
  
# Expose live reload port  
EXPOSE 35729  
WORKDIR /app  
CMD ["/bin/bash", "/run.sh"]  

