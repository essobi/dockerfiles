#  
# SVN Docker container  
#  
# Version 0.1  
FROM debian:8  
MAINTAINER Joseph Lutz <Joseph.Lutz@novatechweb.com>  
  
# install the required packages and cleanup the install  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \  
apache2 \  
enscript \  
libapache2-svn \  
php5-common \  
subversion \  
websvn && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# copy over files  
COPY \  
config/000-default-ssl.conf \  
config/000-default.conf \  
config/000-svn.conf \  
config/000-websvn.conf \  
/etc/apache2/sites-available/  
COPY config/ldap.conf \  
/etc/apache2/mods-available/  
COPY \  
config/config.php \  
/etc/websvn/  
COPY ./docker-entrypoint.sh \  
./configure.sh \  
/  
  
# run the configuration script  
RUN ["/bin/bash", "/configure.sh"]  
  
# specify which network ports will be used  
EXPOSE 80 443  
# specify the volumes directly related to this image  
VOLUME ["/var/lib/svn"]  
  
# start the entrypoint script  
WORKDIR /var/lib/svn  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["svn"]  

