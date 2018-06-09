# base image is Debian  
FROM debian  
  
# environment variables  
ENV SVN_DEFAULT_USER="default" \  
SVN_DEFAULT_USER_PASSWD="default" \  
SVN_REPOSITORIES_DESCR="My repositories" \  
SVN_DEFAULT_REPOSITORY="default"  
# install packages  
RUN apt-get update \  
&& apt-get install -y \  
apache2 \  
libapache2-svn \  
subversion \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# enable a svn module  
RUN a2enmod dav_svn  
  
EXPOSE 80  
COPY ./*.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/apache2foreground.sh"]  

