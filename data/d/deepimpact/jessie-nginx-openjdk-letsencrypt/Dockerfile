FROM openjdk:8u131-jre  
  
ADD run.sh /app/run.sh  
ADD supervisord.conf /etc/supervisord.conf  
  
RUN echo "deb http://packages.dotdeb.org jessie all" >>/etc/apt/sources.list \  
&& echo "deb-src http://packages.dotdeb.org jessie all"
>>/etc/apt/sources.list \  
&& curl https://www.dotdeb.org/dotdeb.gpg > /tmp/dotdeb.gpg \  
&& apt-key add /tmp/dotdeb.gpg \  
&& apt-get update \  
&& apt-get install -y nginx supervisor \  
&& apt-get install -y python-certbot-apache -t jessie-backports \  
&& rm -rf /var/lib/apt/lists/* /tmp/* \  
&& rm /etc/nginx/sites-enabled/default  
  
ADD nginx.conf /etc/nginx/nginx.conf  
  
CMD ["/app/run.sh"]  

