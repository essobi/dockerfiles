FROM java:openjdk-8-jre  
  
MAINTAINER Eugene Volchek <evolchek@klika-tech.com>  
  
ENV UPSOURCE_VERSION 3.0.4396  
WORKDIR /opt  
RUN mkdir -p /home/upsource \  
&& groupadd -g 999 upsource \  
&& useradd -u 999 -g upsource -d /home/upsource upsource \  
&& chown -R upsource:upsource /home/upsource \  
&& wget -nv
http://download.jetbrains.com/upsource/upsource-$UPSOURCE_VERSION.zip \  
&& unzip upsource-$UPSOURCE_VERSION.zip \  
&& mv upsource-$UPSOURCE_VERSION /opt/Upsource \  
&& rm -rf upsource-$UPSOURCE_VERSION.zip \  
&& chown -R upsource:upsource Upsource  
USER upsource  
EXPOSE 8080  
WORKDIR /opt/Upsource  
VOLUME ["/opt/Upsource/conf", "/opt/Upsource/data", "/opt/Upsource/logs",
"/opt/Upsource/backups"]  
CMD ["bin/upsource.sh", "run"]  

