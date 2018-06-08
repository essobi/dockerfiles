FROM debian  
  
RUN apt-get update -y &&\  
apt-get install smokeping sendmail -y  
  
EXPOSE 80  
ENTRYPOINT /etc/init.d/smokeping start && /etc/init.d/apache2 start && tail -f
/var/log/apache2/access.log  

