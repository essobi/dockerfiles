FROM phusion/baseimage:latest  
  
# Set correct environment variables  
ENV DEBIAN_FRONTEND="noninteractive" HOME="/root" LC_ALL="C.UTF-8"
LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"  
ENV db_PORT=tcp://db:3306  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
RUN apt-get update -qq \  
&& apt-get upgrade -qy \  
&& apt-get install -qy \  
apache2 \  
apache2-utils \  
libexpat1 \  
ssl-cert \  
python \  
libapache2-mod-wsgi \  
&& add-apt-repository ppa:privacyidea/privacyidea \  
&& apt-get update -qq \  
&& apt-get install -qy \  
python-privacyidea \  
privacyideaadm  
  
ADD setup.sh /tmp/  
RUN bash /tmp/setup.sh \  
&& mkdir /privacyidea \  
&& chmod -R 755 /privacyidea  
ADD privacyideaapp.wsgi /privacyidea/  
  
#Add Apache configuration  
ADD privacyidea.conf /etc/apache2/sites-available/  
RUN chmod 644 /etc/apache2/sites-available/privacyidea.conf \  
&& chmod 644 /privacyidea/privacyideaapp.wsgi \  
&& a2dissite 000-default \  
&& a2enmod ssl \  
&& a2ensite privacyidea  
  
VOLUME /etc/privacyidea /var/lib/privacyidea /var/log/privacyidea  
  
EXPOSE 443/tcp  

