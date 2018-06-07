FROM durenworks/webphp-dev:0.2.1  
# Docker maintainer  
MAINTAINER Airlangga Cahya Utama <airlangga@durenworks.com>  
  
# Set correct environment variables.  
ENV MYSQL_PASSWORD password1  
  
# Set password  
RUN echo "mysql-server mysql-server/root_password password $MYSQL_PASSWORD" \  
| debconf-set-selections  
RUN echo "mysql-server mysql-server/root_password_again password
$MYSQL_PASSWORD" \  
| debconf-set-selections  
  
# Update repository information  
RUN apt-get update -yq && \  
apt-get install -yq mysql-server && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Copy config file  
COPY build /build  
RUN cp -R /build/etc/* /etc  
  
# Run script to add remote user access  
RUN /build/script/mysql_remote_user.sh  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 3306  

