# Mediawiki-Apache  
#  
# Version 1.0  
  
FROM tutum/apache-php:latest  
MAINTAINER John E Arnold <iohannes.eduardus.arnold@gmail.com>  
  
# Remove the old hello world app and grab Mediawiki source  
RUN rm -fr /app && git clone
https://gerrit.wikimedia.org/r/p/mediawiki/core.git /app  
RUN cd /app && git checkout -b REL1_23 origin/REL1_23  
  
# Create the section for persistent files  
RUN mkdir /var/lib/mediawiki  
# Move the files that need to be persistent and create symbolic links to them  
RUN mv /app/images /var/lib/mediawiki/ && ln -s /var/lib/mediawiki/images
/app/images  
RUN mv /app/skins /var/lib/mediawiki/ && ln -s /var/lib/mediawiki/skins
/app/skins  
RUN touch /var/lib/mediawiki/LocalSettings.php && ln -s
/var/lib/mediawiki/LocalSettings.php /app/LocalSettings.php  
  
EXPOSE 80  
CMD ["/run.sh"]  

