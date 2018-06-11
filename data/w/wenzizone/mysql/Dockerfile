# Mysql  
#  
FROM wenzizone/base  
MAINTAINER wenzizone <wenzizone@126.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install mysql server  
RUN apt-get update && \  
apt-get install -y mysql-server && \  
apt-get clean  
  
ADD my.cnf /etc/mysql/my.cnf  
#RUN sed -i "s/bind/#bind/" /etc/mysql/my.cnf  
ADD launch.bash /launch  
RUN chmod +x /launch  
  
VOLUME ["/var/lib/mysql"]  
  
CMD ["/launch"]

