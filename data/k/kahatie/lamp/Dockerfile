FROM kahatie/debian:jessie  
MAINTAINER kahatie <kahatie@gmail.com>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="lamp" \  
org.label-schema.description="lamp server" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/kahatie/docker" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
ENV SVN_PROD ""  
# Volume home  
VOLUME ["/home/"]  
  
# Mise a jour / installation des packet  
RUN apt-get update && apt-get install -y\  
apache2\  
libapache2-mod-php5\  
php5\  
mysql-server\  
phpmyadmin\  
openssh-server\  
subversion\  
libapache2-svn\  
&& apt-get clean\  
&& rm -rf /var/lib/apt/lists/*  
  
# Copie le fichier de config de supervisord  
COPY supervisord.conf /etc/supervisor/conf.d/debian-lamp.conf  
# Copie les fichiers de config de svn  
COPY dav_svn.conf /etc/apache2/mods-available/dav_svn.conf  
COPY dav_svn.authz /home/svn/dav_svn.authz  
# apache 2 config  
COPY apache2.conf /etc/apache2/apache2.conf  
COPY default.conf /etc/apache2/sites-available/000-default.conf  
#repository config  
COPY post-commit /tmp/hooks/post-commit  
  
# init script  
COPY init.sh /init.sh  
RUN chmod +x /init.sh  
  
# Map port 80 et ssl apache2  
EXPOSE 22 80 443  
CMD ["/init.sh"]  

