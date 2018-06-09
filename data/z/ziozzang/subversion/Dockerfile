FROM ubuntu:14.04  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup  
RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV HOME /root  
  
RUN sed -i 's/archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list  
RUN apt-get update && apt-get -y -o Dpkg::Options::="--force-confold" upgrade  
  
RUN apt-get install -y apache2 subversion libapache2-svn  
  
RUN usermod -U www-data && chsh -s /bin/bash www-data  
#RUN echo 'ServerName ${ENV:SERVERNAME}' >> /etc/apache2/conf-
enabled/servername.conf  
RUN rm /etc/apache2/mods-available/dav_svn.conf  
COPY dav_svn.conf /etc/apache2/mods-available/dav_svn.conf  
RUN a2enmod rewrite cgid headers dav_svn  
RUN a2dissite 000-default  
  
#RUN sed -i 's/ErrorLog.*/ErrorLog \/dev\/null/' /etc/apache2/apache2.conf  
#RUN cat /etc/apache2/apache2.conf  
RUN mkdir -p /etc/svn  
RUN mkdir -p /var/svn  
  
#ENV SERVERNAME "docker-subversion"  
VOLUME /var/svn  
VOLUME /etc/svn  
  
EXPOSE 80  
#USER www-data  
#WORKDIR /var/svn  
ADD start.sh /start.sh  
RUN chmod 755 /start.sh  
  
CMD bash /start.sh  

