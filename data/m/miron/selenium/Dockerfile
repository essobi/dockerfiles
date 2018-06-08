FROM elgalu/selenium:3.8.1-p12  
MAINTAINER miron.ogrodowicz@kreativrudel.de  
  
RUN set -ex; \  
\  
sudo apt-get update; \  
sudo apt-get install -y socat \  
; \  
sudo rm -rf /var/lib/apt/lists/*  
  
ADD ./supervisord/start-socat.sh /start-socat.sh  
  
RUN sudo chmod 755 /start-socat.sh  
  
ADD ./supervisord/supervisord-socat.conf /etc/supervisor/conf.d/  
  
RUN sudo chown seluser: /etc/supervisor/conf.d/supervisord-socat.conf  

