FROM ubuntu:trusty-20160323  
MAINTAINER zhoujunqian <zjqzero@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y install python-dev python-pip nginx libxml2-dev libxslt-dev
zlib1g-dev supervisor openssh-client  
  
RUN pip install fabric-bolt  
  
COPY settings.py /root/.fabric-bolt/  
COPY fabric-bolt.db /root/.fabric-bolt/  
  
RUN mkdir -p /var/www/  
RUN cp -r usr/local/lib/python2.7/dist-packages/fabric_bolt/core/static
/var/www/  
  
RUN rm /etc/nginx/sites-enabled/*  
RUN echo '' >> /etc/nginx/nginx.conf  
RUN echo 'daemon off;' >> /etc/nginx/nginx.conf  
COPY fabric.conf /etc/nginx/conf.d/fabric.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 5000 5001  
WORKDIR /var/www  
  
CMD ["/usr/bin/supervisord"]  

