FROM nginx:1.9  
MAINTAINER "Jasper Lievisse Adriaanse" <j@jasper.la>  
  
RUN apt-get -qqy update && \  
apt-get -qqy install createrepo && \  
apt-get clean  
  
COPY configs/yum.conf /etc/nginx/conf.d/default.conf  
  
VOLUME /var/repo  
  
ADD scripts/run.sh /run.sh  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/run.sh"]  
  

