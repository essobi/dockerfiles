FROM ubuntu:latest  
MAINTAINER Francois Dazan  
  
#Node  
RUN apt-get update && apt-get -y install curl git vim sudo wget && apt-get
clean  
RUN curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash - && apt-get
-y install nodejs  
  
RUN mkdir -p /var/www/html  
COPY app /var/www/html  
WORKDIR /var/www/html  
  
COPY parameters.json /var/www/html/app/config/parameters.json  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /*.sh  
  
RUN npm install && npm install gulp -g  
  
# Expose port  
EXPOSE 8080 1230  
# Executing entrypoint  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Executing node  
CMD ["npm", "start"]  

