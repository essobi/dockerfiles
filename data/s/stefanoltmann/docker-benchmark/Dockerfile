FROM debian:stable  
MAINTAINER Stefan Oltmann <docker@stefan-oltmann.de>  
  
# Update  
RUN apt-get update  
  
# Pakete installieren  
# SSH für Remote Zugriff  
# Apache2 + PHP5 für Webdienste  
# Supervisor um mehrere Dienste gleichzeitig laufen zu lassen  
# BC für den "Benchmark"-Befehl "time echo "scale=1000; 4*a(1)" | bc -l"  
# htop als besseres top  
# screen weil es nützlich ist  
RUN apt-get install -y openssh-server apache2 php5 supervisor bc htop screen
wget  
# Abhängigkeiten von UnixBench (als ernsthafter, schmerzhafter Benchmark)  
RUN apt-get install -y libx11-dev libgl1-mesa-dev libxext-dev perl perl-
modules make gcc  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd
/var/log/supervisor  
  
# Aufräumen  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
  
# Supervisor Config kopieren  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# SSH mit Passwort einrichten  
RUN echo 'root:CQhMcJPxEaA4qcy7fNCHUUrx09urRuteO0UsdMg1JnNs2shWA2' | chpasswd
# Passwort sofort ändern!  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -i 's/#GSSAPIAuthentication no/GSSAPIAuthentication no/'
/etc/ssh/sshd_config  
  
# SSH Login Fix  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# Apache einrichten  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
# Apache SSL aktivieren  
RUN /usr/sbin/a2ensite default-ssl  
RUN /usr/sbin/a2enmod ssl  
  
# php-benchmark-script.com  
COPY bench.php /var/www/html/bench.php  
  
# UnixBench entpacken  
COPY UnixBench /root/UnixBench  
RUN chmod -R 777 /root/UnixBench # fix permissions  
  
# Ports freigeben  
EXPOSE 22 80 443  
VOLUME /root/UnixBench/results  
  
# Dienste starten  
CMD ["/usr/bin/supervisord"]  

