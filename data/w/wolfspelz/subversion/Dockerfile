FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y apache2 subversion libapache2-svn  
  
RUN usermod -U www-data && chsh -s /bin/bash www-data  
  
RUN rm /etc/apache2/mods-available/dav_svn.conf  
RUN a2enmod rewrite cgid headers dav_svn  
#RUN a2dissite 000-default  
RUN echo "Include /etc/svn/*.dav" >> /etc/apache2/apache2.conf  
  
RUN mkdir -p /etc/svn  
RUN mkdir -p /var/svn  
  
COPY sample.dav /var/svn/sample.dav  
COPY svn-access-rw-for-all.txt /etc/svn/svn-access  
  
VOLUME /var/svn  
VOLUME /etc/svn  
  
EXPOSE 80  
ADD start.sh /start.sh  
RUN chmod 755 /start.sh  
  
CMD bash /start.sh  

