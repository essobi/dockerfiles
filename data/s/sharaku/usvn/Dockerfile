FROM php:5.5.30-apache  
MAINTAINER sharaku  
  
# ######################################################################  
  
# update  
RUN apt-get -y update  
  
# Install svn  
RUN apt-get install -y wget subversion libapache2-svn libapache2-mod-encoding
sqlite3  
  
RUN \  
cd /usr/local/src && \  
wget "https://github.com/usvn/usvn/archive/1.0.7.tar.gz" -O usvn-1.0.7.tar.gz
&& \  
tar zxvf usvn-1.0.7.tar.gz && \  
chown -R www-data:www-data /usr/local/src/usvn-1.0.7 && \  
rm -rf /var/www/html  
  
RUN \  
mkdir /var/lib/svn; \  
chown www-data:www-data /var/lib/svn  
  
# start shell  
ADD start.sh /opt/start.sh  
  
# permission setting  
RUN \  
chmod -R 555 /opt/start.sh  
  
# ######################################################################  
# Clear out the local repository of retrieved package files  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# ######################################################################  
# Default configuration: can be overridden at the docker command line  
  
# USVN_SUBDIR /usvn -> http://IP/usvn/  
ENV USVN_SUBDIR ""  
  
# ######################################################################  
# Expose port 80 must  
EXPOSE 80  
  
# ######################################################################  
# data volume  
VOLUME /var/lib/svn  
  
# start  
CMD ["/opt/start.sh"]  
  
#docker build -t sharaku/svn .  
# ----------------  
#docker run -d -v path/to/svn:/var/lib/svn --name usvn -p 80:80 sharaku/usvn  

