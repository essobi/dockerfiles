FROM debian  
MAINTAINER Saul Alonso  
RUN apt-get update  
RUN apt-get install apache2 -y --force-yes  
RUN echo "<h1>Apache con docker</h1> <h2>Hola mundo222!</h2>" >
/var/www/html/index.html  
EXPOSE 80  
ENTRYPOINT apache2ctl -D FOREGROUND  

