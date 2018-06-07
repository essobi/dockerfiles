FROM eboraas/apache  
MAINTAINER Aguay  
RUN echo "deb http://wapt.tranquil.it/debian/ ./ " >
/etc/apt/sources.list.d/wapt.list  
RUN apt -o Acquire::AllowInsecureRepositories=true -o
Acquire::AllowDowngradeToInsecureRepositories=true update \  
&& apt install -y --force-yes tis-waptserver tis-waptrepo tis-waptsetup  
RUN useradd -d /opt/wapt/waptserver waptserver  
RUN chown waptserver -R /opt/wapt/waptserver  
RUN cp /opt/wapt/waptserver/scripts/waptserver-init /etc/init.d/waptserver  
COPY wapt.ini /opt/wapt/conf/waptserver.ini  
COPY apache-wapt.conf /etc/apache2/sites-available/wapt.conf  
RUN a2ensite wapt && a2dissite default-ssl.conf 000-default.conf  
RUN a2enmod proxy proxy_http rewrite deflate headers proxy_html  
EXPOSE 80  
EXPOSE 443  
CMD service mongodb start && sleep 5 && /etc/init.d/waptserver start &&
apache2ctl -D FOREGROUND  

