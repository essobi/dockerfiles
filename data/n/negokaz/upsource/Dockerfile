FROM java:openjdk-8  
MAINTAINER negokaz <negokaz@gmail.com>  
  
ENV UPSOURCE_VERSION 2.0.3554  
VOLUME ["/opt/Upsource/conf", "/opt/Upsource/data", "/opt/Upsource/logs",
"/opt/Upsource/backups"]  
  
# Reference:
https://www.jetbrains.com/upsource/help/2.0/things_to_configure.html  
RUN sed -ri 's/^# End of file$/* - memlock unlimited\n* - nofile 100000\n* -
nproc 32768\n* - as unlimited\n# End of file/' /etc/security/limits.conf  
  
# Reference: https://www.jetbrains.com/upsource/help/2.0/install_on_linux.html  
WORKDIR /opt  
RUN mkdir -p Upsource \  
&& groupadd upsource \  
&& useradd upsource -g upsource \  
&& wget -nv -O Upsource.zip
http://download.jetbrains.com/upsource/upsource-${UPSOURCE_VERSION}.zip \  
&& chmod a+x Upsource.zip \  
&& unzip Upsource.zip \  
&& rm -f Upsource.zip \  
&& chown -R upsource:upsource /opt/Upsource \  
&& chmod -R a+rwX /opt/Upsource  
  
EXPOSE 8080  
ENTRYPOINT ["/opt/Upsource/bin/upsource.sh"]  
  
CMD ["run"]  

