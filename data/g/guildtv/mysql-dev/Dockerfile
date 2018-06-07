FROM mysql:5.5  
MAINTAINER Julian Waller <julian@tech.guildtv.co.uk>  
  
ADD additional.cnf /etc/mysql/conf.d/  
ADD start.sh /  
ADD setup.sh /  
ADD example.sql /  
  
RUN chmod 644 /etc/mysql/conf.d/*  
  
VOLUME /var/lib/mysql  
  
CMD ["/start.sh"]

