FROM frodenas/ubuntu  
MAINTAINER Ferran Rodenas <frodenas@gmail.com>  
  
# Install MySQL 5.6  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --force-yes \  
mysql-server-5.6 && \  
service mysql stop && \  
sed -e 's/^datadir\t.*$/datadir = \/data/' -i /etc/mysql/my.cnf && \  
sed -e 's/^bind-address\t.*$/bind-address = 0.0.0.0/' -i /etc/mysql/my.cnf &&
\  
cp /etc/mysql/my.cnf /usr/share/mysql/my-default.cnf && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add scripts  
ADD scripts /scripts  
RUN chmod +x /scripts/*.sh  
RUN touch /.firstrun  
  
# Command to run  
ENTRYPOINT ["/scripts/run.sh"]  
CMD [""]  
  
# Expose listen port  
EXPOSE 3306  
# Expose our data directory  
VOLUME ["/data", "/var/log/mysql", "/etc/mysql"]  

