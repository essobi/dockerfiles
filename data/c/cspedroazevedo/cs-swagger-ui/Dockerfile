FROM ubuntu  
MAINTAINER "Pedro Cesar" <pedro.azevedo@concretesolutions.com.br>  
  
# UPDATING SYSTEM AND INSTALL PACKAGES  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install unzip nginx -y  
RUN service nginx stop  
  
# CREATE APP STRUCTURE  
RUN mkdir -p /app/swagger  
  
# CONFIGURING WEB SERVER  
ADD conf/swagger /etc/nginx/sites-available/  
RUN cd /etc/nginx/sites-enabled/ && ln -s ../sites-available/swagger  
RUN rm -f /etc/nginx/sites-enabled/default  
RUN echo 'daemon off;' >> /etc/nginx/nginx.conf  
  
# CONFIGURING SWAGGER  
ADD https://github.com/wordnik/swagger-ui/archive/master.zip /app/swagger/  
WORKDIR /app/swagger  
RUN unzip master.zip  
RUN mv swagger-ui-master/dist/* .  
RUN mv index.html aux  
RUN echo "awk -v ENV=\$URL
'{gsub(\"http://petstore.swagger.io/v2/swagger.json\", ENV); print}'
/app/swagger/aux > /app/swagger/index.html ; nginx" > /app/swagger/init_app.sh  
RUN chmod +x /app/swagger/init_app.sh  
  
CMD bash /app/swagger/init_app.sh  

