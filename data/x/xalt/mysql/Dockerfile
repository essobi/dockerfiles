FROM mysql:5.6.32  
MAINTAINER abhishek kapoor abhishek.kapoor@xaltbc.de  
  
#Copy the my.cnf file  
COPY my.cnf /etc/mysql/conf.d  
COPY set-slave.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/set-slave.sh  
RUN ln -s usr/local/bin/set-slave.sh /set-slave.sh  

