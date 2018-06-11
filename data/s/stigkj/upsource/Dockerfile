FROM java:8  
MAINTAINER Stig Kleppe-Jørgensen <from.docker@nisgits.net>  
  
EXPOSE 8080  
VOLUME ["/opt/Upsource/conf", "/opt/Upsource/data", "/opt/Upsource/logs",
"/opt/Upsource/backups"]  
WORKDIR /opt  
ENV UPSOURCE_VERSION 2.0.3653  
RUN groupadd -g 999 upsource \  
&& useradd -u 999 -g 999 -m -d /home/upsource -p dummy upsource \  
&& wget -q
http://download.jetbrains.com/upsource/upsource-$UPSOURCE_VERSION.zip \  
&& unzip upsource-$UPSOURCE_VERSION.zip \  
&& rm -rf upsource-$UPSOURCE_VERSION.zip \  
&& chown -R upsource:upsource /opt/Upsource  
  
USER upsource  
WORKDIR /opt/Upsource  
  
CMD ["bin/upsource.sh", "run"]  

