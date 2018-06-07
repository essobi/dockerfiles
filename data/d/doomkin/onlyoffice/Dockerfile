#  
# doomkin/onlyoffice Dockerfile  
#  
# https://github.com/doomkin/onlyoffice  
#  
# Based on:  
# https://github.com/doomkin/nginx  
# https://github.com/ONLYOFFICE/Docker-ONLYOFFICE-CommonServer  
#  
# Pull base image.  
FROM doomkin/nginx  
MAINTAINER Pavel Nikitin <p.doomkin@ya.ru>  
  
# Set the noninteractive frontend  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update packages  
RUN \  
echo "deb http://download.onlyoffice.com/repo/debian squeeze main" >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D9D0BF019CC8AC0D && \  
apt-get update && apt-get upgrade -y  
  
# Install MySQL, create onlyoffice database, install ONLYOFFICE  
RUN \  
apt-get install -y mysql-server && \  
cd /tmp && \  
service mysql start && \  
echo "mysqladmin --silent --wait=30 ping || exit 1" > config && \  
echo "mysql -e 'CREATE DATABASE onlyoffice CHARACTER SET utf8;'" >> config &&
\  
echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"localhost\" WITH
GRANT OPTION;'" >> config && \  
bash config && \  
rm -f config && \  
apt-get install -yq onlyoffice  
  
# Cleanup  
RUN rm -rf /var/lib/apt/lists/*  
  
# Copy start script  
ADD start.sh /start.sh  
RUN chmod 755 /start.sh  
  
# Expose ports  
EXPOSE 80 443 5222 25 465 143 993 110 995  
# Define default command.  
CMD /start.sh  

