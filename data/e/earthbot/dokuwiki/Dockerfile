FROM aerth/php:latest  
MAINTAINER aerth@sdf.org  
WORKDIR /var/www  
RUN rm -Rf /var/www/public  
ADD https://github.com/splitbrain/dokuwiki/tarball/stable
/var/www/dokuwiki.tgz  
RUN tar -xzf dokuwiki.tgz && \  
mv splitbrain-* /var/www/public && \  
rm dokuwiki.tgz && \  
chown -R nginx:nginx /var/www/public  
RUN mkdir /dokuwiki-storage && \  
mv /var/www/public/conf /dokuwiki-storage/conf && \  
ln -s /dokuwiki-storage/conf /var/www/public/conf && \  
mv /var/www/public/data /dokuwiki-storage/data && \  
ln -s /dokuwiki-storage/data /var/www/public/data && \  
mv /var/www/public/lib/plugins /dokuwiki-storage/plugins && \  
ln -s /dokuwiki-storage/plugins /var/www/public/lib/plugins  
#VOLUME ["/dokuwiki-storage"]  
EXPOSE 80  
CMD ["/run.sh"]  

