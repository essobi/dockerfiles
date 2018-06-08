FROM ubuntu:quantal  
MAINTAINER jean-vincent KASSI <jeanvincent45@gmail.com>  
  
RUN apt-get update -qq && apt-get install -y mysql-server supervisor  
  
# serf stuff  
ADD /serf /usr/bin/  
ADD /start-serf.sh /start-serf.sh  
ADD /serf-join.sh /serf-join.sh  
ADD /supervisord-serf.conf /etc/supervisor/conf.d/supervisord-serf.conf  
  
# mysql stuff  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
RUN chmod 664 /etc/mysql/conf.d/my.cnf  
ADD run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
RUN chmod +x /*.sh  
  
VOLUME ["/var/lib/mysql"]  
EXPOSE 3306  
CMD ["/usr/local/bin/run"]  

