FROM ubuntu:14.04  
EXPOSE 80  
RUN apt-get update && \  
apt-get install -y \  
apache2 \  
libc6-i386 \  
libx11-6 \  
libxext6 \  
unzip \  
wget  
  
RUN mkdir -p /usr/local/livecode && cd /usr/local/livecode && \  
wget
"http://livecodestatic.com/downloads/livecode/8_1_5/LiveCodeCommunityServer-8_1_5_rc_1-Linux-x86_64.zip"
&& \  
unzip LiveCodeCommunityServer-8_1_5_rc_1-Linux-x86_64.zip && \  
chmod 755 livecode-community-server && \  
a2enmod actions && a2enmod cgi  
  
COPY apache2/apache2.conf /etc/apache2/apache2.conf  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_RUN_DIR=/var/run/apache2  
  
ENTRYPOINT ["/usr/sbin/apache2"]  
CMD ["-D", "FOREGROUND"]  

