FROM athimel/nginx-php  
MAINTAINER Arnaud Thimel <a.thimel@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Wget in order to download dokuwiki  
RUN apt-get update && apt-get install -y wget && apt-get clean  
  
# Download and uncompress  
RUN wget http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz -O
dokuwiki-stable.tgz  
RUN tar -zxf dokuwiki-stable.tgz  
RUN rm dokuwiki-stable.tgz  
  
# Install  
RUN rm -rf /var/www/html  
# NB : the name is probably something like dokuwiki-2015-08-10a  
RUN mv dokuwiki-* /var/www/html  
RUN chown -R www-data:www-data /var/www/html  
  
EXPOSE 80  
ENTRYPOINT ["/root/run.sh"]  
  

