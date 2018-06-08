FROM ruby:2.3.1  
MAINTAINER Leandro Di Tommaso <leandro.ditommaso@mikroways.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -qy \  
apache2-utils \  
nginx-extras \  
nodejs \  
sudo && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD nginx.conf /etc/nginx/  
ADD default.conf /etc/nginx/conf.d/  
ADD ./generate-html.sh /bin/  
ADD ./entrypoint.sh /bin/  
RUN mkdir /data && \  
rm /etc/nginx/sites-enabled/default && \  
chmod +x /bin/generate-html.sh && \  
chmod +x /bin/entrypoint.sh  
  
EXPOSE "80"  
ENTRYPOINT ["/bin/entrypoint.sh"]  

