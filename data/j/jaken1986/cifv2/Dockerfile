FROM aeppert/cifv2  
  
MAINTAINER jaken1986 version: 0.1  
  
RUN rm /start.sh  
  
ADD crontab /etc/cron.d/cif-script  
ADD start.sh /start.sh  
  
RUN add-apt-repository ppa:0k53d-karl-f830m/openssl && \  
apt-get update && apt-get -y install tidy apache2 openssl && \  
apt-get clean && \  
chmod 0644 /etc/cron.d/cif-script && \  
touch /home/cif/feeds.sh && \  
chown cif:cif /home/cif/feeds.sh && \  
chmod +x /home/cif/feeds.sh && \  
chmod 755 /start.sh && \  
cpanm https://github.com/csirtgadgets/p5-cif-sdk/archive/2.02.tar.gz  

