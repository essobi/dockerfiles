FROM ubuntu:16.04  
MAINTAINER su-kun1899 <higedrum.coz@gmail.com>  
  
# Enable add-apt-repository  
RUN apt-get update  
RUN apt-get -y install python-software-properties software-properties-common  
  
# Locale  
RUN locale-gen en_US.UTF-8  
ENV LANG=en_US.UTF-8  
# Install mysql  
RUN add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe'  
RUN apt-get update  
RUN echo "mysql-server-5.6 mysql-server/root_password password root" |
debconf-set-selections  
RUN echo "mysql-server-5.6 mysql-server/root_password_again password root" |
debconf-set-selections  
RUN apt-get -y --no-install-recommends install mysql-server-5.6  
RUN mkdir /home/mysql  
RUN chown mysql /home/mysql/  
RUN chgrp mysql /home/mysql/  
RUN usermod -d /home/mysql/ mysql  
RUN touch /var/lib/mysql/mysql.sock  
RUN chown mysql:mysql /var/lib/mysql/mysql.sock  
  
# Initialize mysql  
COPY my.cnf /etc/mysql/my.cnf  
RUN /etc/init.d/mysql start && mysql -uroot -proot -e "GRANT ALL PRIVILEGES ON
*.* TO 'root'@'%' WITH GRANT OPTION; FLUSH PRIVILEGES;"  
  
COPY startup.bash /  
  
EXPOSE 3306  
CMD ["/startup.bash"]  

