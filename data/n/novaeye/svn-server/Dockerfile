FROM alpine:latest  
MAINTAINER novaeye <novaeye@qq.com>  
  
ENV SVN_URI_PREFIX=svn  
  
RUN apk add --update apache2 apache2-utils apache2-webdav mod_dav_svn
subversion && \  
rm /var/cache/apk/* && \  
mkdir -p /run/apache2 && \  
mkdir -p /data/svn && \  
rm -rf /etc/apache2/conf.d/subversion.conf  
  
COPY subversion.conf /etc/apache2/conf.d/subversion.conf.template  
  
VOLUME /data/svn  
  
ADD startup.sh /startup.sh  
  
RUN chmod +x /startup.sh  
  
EXPOSE 80  
CMD ["/startup.sh"]  

