FROM ubuntu:latest  
RUN apt-get update && apt-get install -y python3 apache2 python3-matplotlib
multitail  
RUN a2enmod cgid  
COPY ./html/ /var/www/html/  
COPY ./cgi-bin/ /usr/lib/cgi-bin/  
EXPOSE 80  
ENV NAME "A Quantum Particle Moving in Space"  
#CMD service apache2 start; multitail -i /var/log/apache2/access.log -I
/var/log/apache2/error.log -I /var/log/apache2/other_vhosts_access.log  
CMD service apache2 start; sleep infinity  

