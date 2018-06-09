# Dockerizing Subversion: Dockerfile for building Subversion images  
# Based on ubuntu:16.04, installs Subversion  
FROM ubuntu:16.04  
# Installation:  
# Install apache  
RUN apt-get -y update && apt-get -y install apache2  
  
# Install subversion e DAV module  
RUN apt-get -y install subversion libapache2-mod-svn libapache2-svn libsvn-dev  
RUN a2enmod dav  
RUN a2enmod dav_svn  
  
# Copy file with DAV configuration  
COPY dav_svn.conf /etc/apache2/mods-enabled/  
  
# Create the MongoDB data directory  
RUN mkdir -p /var/data/svn  
  
# Create a volume  
VOLUME ["/var/data/svn"]  
  
# Create a repo  
RUN svnadmin create /var/data/svn/repo  
RUN chown -R www-data:www-data /var/data/svn  
RUN chmod -R 777 /var/data/svn  
RUN htpasswd -bcm /etc/apache2/dav_svn.passwd admin admin1234  
  
# Expose port #80 from the container to the host  
EXPOSE 80  
# Set /usr/bin/mongod as the dockerized entry-point application  
ENTRYPOINT ["/usr/sbin/apache2ctl","-D", "FOREGROUND"]  

