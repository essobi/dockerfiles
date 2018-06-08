FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install -y pgbouncer  
ADD pgbouncer.ini /etc/pgbouncer/pgbouncer.ini  
ADD userlist.txt /etc/pgbouncer/userlist.txt  
ADD run.sh /root/run.sh  
RUN chmod +x /root/run.sh  
EXPOSE 5431/tcp  
CMD ["/root/run.sh"]  

