FROM ubuntu:trusty  
  
# Set environment variables  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install packages  
RUN apt-get update && apt-get install -y software-properties-common  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db  
RUN add-apt-repository -y 'deb
http://ams2.mirrors.digitalocean.com/mariadb/repo/10.0/ubuntu trusty main'  
RUN apt-get update && apt-get install -y mariadb-server pwgen  
  
# Prepare directories  
RUN mkdir -p /scripts  
RUN mkdir -p /databases  
  
# Add scripts  
ADD scripts/run.sh /scripts/run.sh  
ADD scripts/do_db_tasks.sh /scripts/do_db_tasks.sh  
ADD scripts/create_databases.sh /scripts/create_databases.sh  
ADD scripts/create_mariadb_admin_user.sh /scripts/create_mariadb_admin_user.sh  
  
# Change permissions on scripts  
RUN chown -Rf root:root /scripts  
RUN chmod -Rf 755 /scripts  
  
# Change bind address to 0.0.0.0  
RUN sed -i -r 's/bind-address.*$/bind-address = 0.0.0.0/' /etc/mysql/my.cnf  
  
# Workaround for mysql client error message "TERM environment variable not
set"  
ENV TERM dumb  
  
# Expose the mysql port  
EXPOSE 3306  
# Run the initial script  
CMD ["/scripts/run.sh"]  

